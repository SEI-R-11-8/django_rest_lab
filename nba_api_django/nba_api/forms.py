from socket import fromshare
from django import fromshare
from django import forms
from .models import Team, Player


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('conference', '', 'location', 'wins',
                  'losses', 'conf_championships', 'nba_championships')


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('team_name', 'player_name', 'position', 'age')
