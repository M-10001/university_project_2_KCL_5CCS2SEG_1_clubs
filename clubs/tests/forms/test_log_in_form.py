from django import forms
from django.test import TestCase
from clubs.forms import LogInForm
from django.urls import reverse
from clubs.models import User
from clubs.tests.helpers import LogInTester

class LogInFormTestCase(TestCase, LogInTester):
    """Unit tests of the log in form."""

    fixtures = ['clubs/tests/fixtures/other_users.json']

    def setUp(self):
        self.form_input = {'email': 'test1@example.org','password': 'Password123'}

    def test_form_contains_required_fields(self):
        form = LogInForm()
        self.assertIn('email', form.fields)
        self.assertIn('password', form.fields)
        password_field = form.fields['password']
        self.assertTrue(isinstance(password_field.widget,forms.PasswordInput))

    def test_form_accepts_valid_input(self):
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_rejects_blank_email(self):
        self.form_input['email'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_rejects_blank_password(self):
        self.form_input['password'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_accepts_incorrect_email(self):
        self.form_input['email'] = 'ma'
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_accepts_incorrect_password(self):
        self.form_input['password'] = 'pwd'
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_can_authenticate_valid_user(self):
        fixture = User.objects.get(email='test2@example.org')
        form_input = {'email': 'test2@example.org', 'password': 'Password123'}
        form = LogInForm(data=form_input)
        user = form.get_user()
        self.assertEqual(user, fixture)

    def test_invalid_credentials_do_not_authenticate(self):
        form_input = {'email': 'test2@example.org', 'password': 'WrongPassword123'}
        form = LogInForm(data=form_input)
        user = form.get_user()
        self.assertEqual(user, None)

    def test_blank_password_does_not_authenticate(self):
        form_input = {'email': 'test2@example.org', 'password': ''}
        form = LogInForm(data=form_input)
        user = form.get_user()
        self.assertEqual(user, None)

    def test_blank_email_does_not_authenticate(self):
        form_input = {'email': '', 'password': 'Password123'}
        form = LogInForm(data=form_input)
        user = form.get_user()
        self.assertEqual(user, None)
