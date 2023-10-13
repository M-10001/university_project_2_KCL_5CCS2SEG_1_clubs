# Generated by Django 3.2.5 on 2021-12-17 02:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0033_auto_20211217_0227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['number']},
        ),
        migrations.RenameField(
            model_name='group',
            old_name='group_type',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_number',
        ),
        migrations.AddField(
            model_name='group',
            name='number',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Group number, can not be lower than 1.')]),
        ),
    ]