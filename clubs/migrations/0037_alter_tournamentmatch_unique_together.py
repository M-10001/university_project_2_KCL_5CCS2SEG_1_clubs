# Generated by Django 3.2.5 on 2021-12-17 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0036_alter_group_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tournamentmatch',
            unique_together={('group', 'player1', 'player2')},
        ),
    ]
