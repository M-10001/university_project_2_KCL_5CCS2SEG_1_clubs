# Generated by Django 3.2.5 on 2021-12-14 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0013_tournamentmatch_tournament'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together={('tournament', 'membership')},
        ),
    ]
