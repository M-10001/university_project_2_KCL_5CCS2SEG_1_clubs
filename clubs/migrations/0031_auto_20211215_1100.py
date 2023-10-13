# Generated by Django 3.2.5 on 2021-12-15 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0030_alter_tournament_co_organisers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='membership',
            new_name='member',
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together={('tournament', 'member')},
        ),
    ]
