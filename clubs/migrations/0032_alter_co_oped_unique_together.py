# Generated by Django 3.2.5 on 2021-12-15 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0031_auto_20211215_1100'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='co_oped',
            unique_together={('tournament', 'co_organiser')},
        ),
    ]
