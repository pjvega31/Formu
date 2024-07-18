# myapp/forms.py

from django import forms
from .models import RacePicks, Driver, Constructor

class RacePicksForm(forms.ModelForm):
    class Meta:
        model = RacePicks
        exclude = ['user']  # Excluye el campo de usuario para que no aparezca en el formulario

    def __init__(self, *args, **kwargs):
        super(RacePicksForm, self).__init__(*args, **kwargs)
        self.fields['team_1'].queryset = Constructor.objects.filter(rank__lte=5)
        self.fields['team_2'].queryset = Constructor.objects.filter(rank__gte=6, rank__lte=8)
        self.fields['team_3'].queryset = Constructor.objects.filter(rank__gte=9)
        self.fields['red_bull_racing_driver'].queryset = Driver.objects.filter(team__name='Red Bull Racing')
        self.fields['scuderia_ferrari_driver'].queryset = Driver.objects.filter(team__name='Scuderia Ferrari')
        self.fields['mclaren_racing_driver'].queryset = Driver.objects.filter(team__name='McLaren Racing')
        self.fields['mercedes_amg_petronas_driver'].queryset = Driver.objects.filter(team__name='Mercedes AMG Petronas')
        self.fields['aston_martin_driver'].queryset = Driver.objects.filter(team__name='Aston Martin')
        self.fields['alpine_driver'].queryset = Driver.objects.filter(team__name='Alpine')
        self.fields['visa_cash_app_rb_driver'].queryset = Driver.objects.filter(team__name='Visa Cash App RB')
        self.fields['kick_sauber_driver'].queryset = Driver.objects.filter(team__name='Kick Sauber')
        self.fields['haas_driver'].queryset = Driver.objects.filter(team__name='Haas')
        self.fields['williams_driver'].queryset = Driver.objects.filter(team__name='Williams')
        self.fields['fastest_lap_driver'].queryset = Driver.objects.all()
