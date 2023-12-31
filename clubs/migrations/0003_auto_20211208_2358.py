# Generated by Django 3.2.5 on 2021-12-08 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20211207_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='chess_experience_level',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contact_details',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='personal_statement',
        ),
        migrations.AddField(
            model_name='membership',
            name='member_bio',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='membership',
            name='member_chess_experience_level',
            field=models.IntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Expert'), (3, 'Master')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='member_contact_details',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='member_first_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='member_last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='member_personal_statement',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
