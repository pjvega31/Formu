# myapp/management/commands/generate_matchups.py
from django.core.management.base import BaseCommand
from myapp.models import Race, Team, Matchup

class Command(BaseCommand):
    help = 'Generate matchups for races'

    def handle(self, *args, **kwargs):
        teams = list(Team.objects.all())
        races = Race.objects.all()

        for race in races:
            if len(teams) % 2 != 0:
                teams.append(None)  # Añadir un bye si hay un número impar de equipos

            half = len(teams) // 2
            for i in range(half):
                team_a = teams[i]
                team_b = teams[-i-1]
                if team_a and team_b:
                    matchup, created = Matchup.objects.get_or_create(race=race, team_a=team_a, team_b=team_b)
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Created matchup: {team_a.name} vs {team_b.name} for race {race.name}'))

        self.stdout.write(self.style.SUCCESS('All matchups generated'))


