# myapp/serializers.py

from rest_framework import serializers
from .models import Constructor, Team, Driver, Race, RacePicks, RaceResult, SprintResult, Matchup

class ConstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constructor
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'

class RacePicksSerializer(serializers.ModelSerializer):
    class Meta:
        model = RacePicks
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Team 1: Constructor ranks 1 to 5
        self.fields['team_1'].queryset = Constructor.objects.filter(rank__lte=5)

        # Team 2: Constructor ranks 6 to 8
        self.fields['team_2'].queryset = Constructor.objects.filter(rank__gte=6, rank__lte=8)

        # Team 3: Constructor ranks 9 to 10
        self.fields['team_3'].queryset = Constructor.objects.filter(rank__gte=9)

        # Red Bull Racing drivers
        self.fields['red_bull_racing_driver'].queryset = Driver.objects.filter(team__name='Red Bull Racing')

        # Scuderia Ferrari drivers
        self.fields['scuderia_ferrari_driver'].queryset = Driver.objects.filter(team__name='Scuderia Ferrari')

        # McLaren Racing drivers
        self.fields['mclaren_racing_driver'].queryset = Driver.objects.filter(team__name='McLaren Racing')

        # Mercedes AMG Petronas drivers
        self.fields['mercedes_amg_petronas_driver'].queryset = Driver.objects.filter(team__name='Mercedes AMG Petronas')

        # Aston Martin drivers
        self.fields['aston_martin_driver'].queryset = Driver.objects.filter(team__name='Aston Martin')

        # Alpine drivers
        self.fields['alpine_driver'].queryset = Driver.objects.filter(team__name='Alpine')

        # Visa Cash App RB drivers
        self.fields['visa_cash_app_rb_driver'].queryset = Driver.objects.filter(team__name='Visa Cash App RB')

        # Kick Sauber drivers
        self.fields['kick_sauber_driver'].queryset = Driver.objects.filter(team__name='Kick Sauber')

        # Haas drivers
        self.fields['haas_driver'].queryset = Driver.objects.filter(team__name='Haas')

        # Williams drivers
        self.fields['williams_driver'].queryset = Driver.objects.filter(team__name='Williams')

        # Fastest lap drivers: all drivers
        self.fields['fastest_lap_driver'].queryset = Driver.objects.all()

class RaceResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceResult
        fields = '__all__'

class SprintResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprintResult
        fields = '__all__'

class MatchupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matchup
        fields = '__all__'




