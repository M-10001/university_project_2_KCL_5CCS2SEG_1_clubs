# Generated by Django 3.2.5 on 2021-12-15 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0024_auto_20211215_0714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='win',
            new_name='won',
        ),
    ]
