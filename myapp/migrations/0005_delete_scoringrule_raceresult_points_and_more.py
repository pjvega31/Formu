# Generated by Django 5.0.7 on 2024-07-14 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_driver_dnf_driver_points_matchup_winner_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ScoringRule',
        ),
        migrations.AddField(
            model_name='raceresult',
            name='points',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sprintresult',
            name='points',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='matchup',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchup_team_a', to='myapp.team'),
        ),
        migrations.AlterField(
            model_name='matchup',
            name='team_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchup_team_b', to='myapp.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='points',
            field=models.FloatField(default=0),
        ),
    ]
