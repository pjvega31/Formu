# myapp/scripts.py

from django.core.management.base import BaseCommand
from myapp.models import SprintResult, Race

class Command(BaseCommand):
    help = 'Eliminar registros problemáticos de SprintResult'

    def handle(self, *args, **kwargs):
        invalid_sprint_results = SprintResult.objects.exclude(race__in=Race.objects.all())
        count = invalid_sprint_results.count()
        invalid_sprint_results.delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} problematic SprintResult records'))
