from django import forms
from .models import Players, Team


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Players
        fields = ('name', 'team', 'position', 'age', 'gp',
                  'injured_reserved', 'points', 'photo_url')


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'location', 'conference',
                  'wins', 'losses', 'photo_url')
