# Generated by Django 3.2.5 on 2021-12-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_tournament_applicant_amount_limit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='applicant_amount_limit',
            new_name='participant_amount_limit',
        ),
    ]