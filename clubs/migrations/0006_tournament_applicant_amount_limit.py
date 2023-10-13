# Generated by Django 3.2.5 on 2021-12-13 08:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_tournament_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='applicant_amount_limit',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=2, message='Total number of applicants, can not be lower than 2.'), django.core.validators.MaxValueValidator(limit_value=96, message='Total number of applicants, can not be greater than 96.')]),
            preserve_default=False,
        ),
    ]