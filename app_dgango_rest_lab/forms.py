from django import forms
from .models import Team, Player

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'location')


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('team', 'position', 'age')