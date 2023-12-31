# Generated by Django 3.2.5 on 2021-12-17 02:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0032_alter_co_oped_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['group_number']},
        ),
        migrations.AddField(
            model_name='group',
            name='group_number',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Group number, can not be lower than 1.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='group_type',
            field=models.IntegerField(choices=[(0, 'Group'), (1, 'Quarter final'), (2, 'Semi final'), (3, 'Final')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
