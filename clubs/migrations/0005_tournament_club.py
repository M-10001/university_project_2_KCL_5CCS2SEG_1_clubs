# Generated by Django 3.2.5 on 2021-12-13 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20211213_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='club',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='clubs.club'),
            preserve_default=False,
        ),
    ]
