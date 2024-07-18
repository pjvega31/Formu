# Generated by Django 5.0.7 on 2024-07-14 15:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Constructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('has_sprint', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ScoringRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('points_race', models.FloatField()),
                ('points_sprint', models.FloatField()),
                ('points_fastest_lap_race', models.FloatField()),
                ('points_fastest_lap_sprint', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.constructor')),
            ],
        ),
        migrations.CreateModel(
            name='RacePicks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpine_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='alpine_driver', to='myapp.driver')),
                ('aston_martin_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='aston_martin_driver', to='myapp.driver')),
                ('fastest_lap_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fastest_lap_driver', to='myapp.driver')),
                ('haas_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='haas_driver', to='myapp.driver')),
                ('kick_sauber_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='kick_sauber_driver', to='myapp.driver')),
                ('mclaren_racing_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mclaren_racing_driver', to='myapp.driver')),
                ('mercedes_amg_petronas_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mercedes_amg_petronas_driver', to='myapp.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.race')),
                ('red_bull_racing_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='red_bull_racing_driver', to='myapp.driver')),
                ('scuderia_ferrari_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='scuderia_ferrari_driver', to='myapp.driver')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='myapp.constructor')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to='myapp.constructor')),
                ('team_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_3', to='myapp.constructor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visa_cash_app_rb_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='visa_cash_app_rb_driver', to='myapp.driver')),
                ('williams_driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='williams_driver', to='myapp.driver')),
            ],
        ),
        migrations.CreateModel(
            name='RaceResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('is_dnf', models.BooleanField(default=False)),
                ('is_fastest_lap', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.race')),
            ],
        ),
        migrations.CreateModel(
            name='SprintResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('is_dnf', models.BooleanField(default=False)),
                ('is_fastest_lap', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.race')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.race')),
                ('team_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_a', to='myapp.team')),
                ('team_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_b', to='myapp.team')),
            ],
        ),
    ]
