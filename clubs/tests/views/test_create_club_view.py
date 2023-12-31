from django.test import TestCase
from django.urls import reverse
from clubs.forms import ClubCreationForm, MembershipOwnerSignUpForm
from clubs.models import User, Club, Membership
from clubs.tests.helpers import LogInTester, reverse_with_next

class CreateClubViewTestCase(TestCase,LogInTester):
    """Tests of the create club view."""

    fixtures = ['clubs/tests/fixtures/default_user.json',
                'clubs/tests/fixtures/other_users.json'
        ]

    def setUp(self):
        self.url = reverse('create_club')
        self.user = User.objects.get(email = 'test1@example.org')
        self.user2 = User.objects.get(email = 'test2@example.org')
        self.form_input = {
            'club_form-name': 'Test Chess Club',
            'club_form-location': 'Test location 555',
            'club_form-description': 'This is a test club.',
            'ownership_form-member_first_name' : 'first_name1',
            'ownership_form-member_last_name':'last_name1',
            'ownership_form-member_contact_details':'0712345678',
            'ownership_form-member_personal_statement':'My personal statement',
            'ownership_form-member_bio':'my bio',
            'ownership_form-member_chess_experience_level':'0'
        }

    def test_create_club_url(self):
        self.assertEqual(self.url,'/create_club/')

    def test_get_create_club_when_logged_in(self):
        self.client.login(username=self.user.email, password="Password123")
        self.assertTrue(self._is_logged_in())
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_club.html')
        club_form = response.context['club_form']
        self.assertTrue(isinstance(club_form, ClubCreationForm))
        ownership_form = response.context['ownership_form']
        self.assertTrue(isinstance(ownership_form, MembershipOwnerSignUpForm))
        self.assertFalse(club_form.is_bound)
        self.assertFalse(ownership_form.is_bound)

    def test_get_create_club_when_not_logged_in(self):
        self.assertFalse(self._is_logged_in())
        response = self.client.get(self.url)
        response_url = reverse_with_next('log_in',self.url)
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)

    def test_successful_create_club_and_ownership(self):
        self.client.login(username=self.user.email, password="Password123")
        self.assertTrue(self._is_logged_in())
        club_before_count = Club.objects.count()
        membership_before_count = Membership.objects.count()
        response = self.client.post(self.url,self.form_input,follow=True)
        club_after_count = Club.objects.count()
        membership_after_count = Membership.objects.count()
        self.assertEqual(club_after_count, club_before_count+1)
        self.assertEqual(membership_after_count, membership_before_count+1)
        club = Club.objects.get(name = 'Test Chess Club')
        self.assertEqual(club.name,"Test Chess Club")
        self.assertEqual(club.location,"Test location 555")
        self.assertEqual(club.description,"This is a test club.")
        membership = Membership.objects.get(club = club, member = self.user)
        self.assertEqual(membership.member_first_name,"first_name1")
        self.assertEqual(membership.member_last_name,"last_name1")
        self.assertEqual(membership.member_contact_details,"0712345678")
        self.assertEqual(membership.member_personal_statement,"My personal statement")
        self.assertEqual(membership.member_bio,"my bio")
        self.assertEqual(membership.member_chess_experience_level,0)
        response_url = reverse('club_page', kwargs = {'club_id' : club.id})
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'club_page.html')

    def test_unsuccessful_create_club_and_ownership(self):
        self.client.login(username=self.user.email, password="Password123")
        self.assertTrue(self._is_logged_in())
        self.form_input['club_form-name'] = ""
        club_before_count = Club.objects.count()
        membership_before_count = Membership.objects.count()
        response = self.client.post(self.url,self.form_input,follow=True)
        club_after_count = Club.objects.count()
        membership_after_count = Membership.objects.count()
        self.assertEqual(club_after_count, club_before_count)
        self.assertEqual(membership_after_count, membership_before_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_club.html')
        club_form = response.context['club_form']
        self.assertTrue(isinstance(club_form, ClubCreationForm))
        ownership_form = response.context['ownership_form']
        self.assertTrue(isinstance(ownership_form, MembershipOwnerSignUpForm))
        self.assertTrue(club_form.is_bound)
        self.assertTrue(ownership_form.is_bound)

    def test_cannot_create_club_and_ownership_for_others(self):
        self.client.login(username=self.user.email, password="Password123")
        self.assertTrue(self._is_logged_in())
        self.form_input['user'] = self.user2
        club_before_count = Club.objects.count()
        membership_before_count = Membership.objects.count()
        response = self.client.post(self.url,self.form_input,follow=True)
        club_after_count = Club.objects.count()
        membership_after_count = Membership.objects.count()
        self.assertEqual(club_after_count, club_before_count+1)
        self.assertEqual(membership_after_count, membership_before_count+1)
        new_membership = Membership.objects.latest('member')
        self.assertTrue(new_membership.is_club_owner())
        self.assertEqual(self.user, new_membership.member)
