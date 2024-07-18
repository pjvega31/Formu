from django.core.management.base import BaseCommand
from myapp.models import SprintResult, Race

class Command(BaseCommand):
    help = 'Clean data with invalid foreign key references'

    def handle(self, *args, **kwargs):
        invalid_sprint_results = SprintResult.objects.exclude(race__in=Race.objects.all())
        invalid_sprint_results_count = invalid_sprint_results.count()
        invalid_sprint_results.delete()
        self.stdout.write(f"Deleted {invalid_sprint_results_count} invalid SprintResult records.")
