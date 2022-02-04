from django import forms
from .models import Team, Player, Conference

class TeamForm(forms.ModelForm):
  
    class Meta:
        model = Team
        fields = ('name', 'location', 'number_of_wins', 'number_of_loses', 'player',)

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'team', 'position', 'age', 'available_for_draft',)

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ('name', 'team',)