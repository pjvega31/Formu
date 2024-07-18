# myapp/admin.py

from django.contrib import admin
from .models import Constructor, Team, Driver, Race, RacePicks, RaceResult, SprintResult, Matchup
from .forms import RacePicksForm

class ConstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank')
    search_fields = ('name',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'wins', 'points')
    search_fields = ('name', 'user__username')
    list_filter = ('wins', 'points')

class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'dnf', 'points')
    search_fields = ('name', 'team__name')
    list_filter = ('team', 'dnf', 'points')

class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'has_sprint')
    search_fields = ('name',)
    list_filter = ('date', 'has_sprint')

class RacePicksAdmin(admin.ModelAdmin):
    form = RacePicksForm
    list_display = ('user', 'race', 'team_1', 'team_2', 'team_3', 'fastest_lap_driver')
    search_fields = ('user__username', 'race__name')
    list_filter = ('race', 'team_1', 'team_2', 'team_3')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

class RaceResultAdmin(admin.ModelAdmin):
    list_display = ('race', 'driver', 'position', 'is_dnf', 'is_fastest_lap', 'points')
    search_fields = ('race__name', 'driver__name')
    list_filter = ('race', 'position', 'is_dnf', 'is_fastest_lap')

class SprintResultAdmin(admin.ModelAdmin):
    list_display = ('race', 'driver', 'position', 'is_dnf', 'is_fastest_lap', 'points')
    search_fields = ('race__name', 'driver__name')
    list_filter = ('race', 'position', 'is_dnf', 'is_fastest_lap')

class MatchupAdmin(admin.ModelAdmin):
    list_display = ('race', 'team_a', 'team_b', 'winner')
    search_fields = ('race__name', 'team_a__name', 'team_b__name')
    list_filter = ('race', 'winner')

admin.site.register(Constructor, ConstructorAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(RacePicks, RacePicksAdmin)
admin.site.register(RaceResult, RaceResultAdmin)
admin.site.register(SprintResult, SprintResultAdmin)
admin.site.register(Matchup, MatchupAdmin)
