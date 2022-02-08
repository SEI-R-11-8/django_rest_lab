from django import forms
from .models import Team, Player

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'location', 'wins', 'loses')

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'position', 'age', 'injured') 