# myapp/views.py

from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Constructor, Team, Driver, Race, RacePicks, RaceResult, SprintResult, Matchup
from .forms import RacePicksForm
from .serializers import (
    ConstructorSerializer, TeamSerializer, DriverSerializer, RaceSerializer,
    RacePicksSerializer, RaceResultSerializer, SprintResultSerializer, MatchupSerializer
)

class ConstructorViewSet(viewsets.ModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RacePicksViewSet(viewsets.ModelViewSet):
    queryset = RacePicks.objects.all()
    serializer_class = RacePicksSerializer

class RaceResultViewSet(viewsets.ModelViewSet):
    queryset = RaceResult.objects.all()
    serializer_class = RaceResultSerializer

class SprintResultViewSet(viewsets.ModelViewSet):
    queryset = SprintResult.objects.all()
    serializer_class = SprintResultSerializer

class MatchupViewSet(viewsets.ModelViewSet):
    queryset = Matchup.objects.all()
    serializer_class = MatchupSerializer

@method_decorator(login_required, name='dispatch')
class AddRacePicksView(View):
    def get(self, request):
        form = RacePicksForm()
        return render(request, 'add_race_picks.html', {'form': form})

    def post(self, request):
        form = RacePicksForm(request.POST)
        if form.is_valid():
            race_pick = form.save(commit=False)
            race_pick.user = request.user  # Asigna el usuario actual
            race_pick.save()
            return redirect('success_url')  # Cambia 'success_url' al nombre de tu URL de éxito
        return render(request, 'add_race_picks.html', {'form': form})

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')
