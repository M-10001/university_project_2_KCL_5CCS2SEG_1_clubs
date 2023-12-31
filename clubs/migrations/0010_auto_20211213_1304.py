# Generated by Django 3.2.5 on 2021-12-13 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0009_alter_tournament_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_in_group', models.FloatField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.group')),
            ],
        ),
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concluded', models.BooleanField(default=False)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_for_player1', to='clubs.grouping')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_for_player2', to='clubs.grouping')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eliminated', models.BooleanField(default=False)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.membership')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.tournament')),
            ],
        ),
        migrations.AddField(
            model_name='grouping',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.participant'),
        ),
        migrations.AlterUniqueTogether(
            name='grouping',
            unique_together={('group', 'participant')},
        ),
    ]
