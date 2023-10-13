# Generated by Django 3.2.5 on 2021-12-14 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0016_alter_tournament_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentmatch',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_as_player1', to='clubs.grouping'),
        ),
        migrations.AlterField(
            model_name='tournamentmatch',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_as_player2', to='clubs.grouping'),
        ),
    ]
