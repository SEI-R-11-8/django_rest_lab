from rest_framework import serializers
from .models import Players, Team


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )

    class Meta:
        model = Players
        fields = ('name', 'teams', 'position', 'age', 'gp',
                  'injured_reserved', 'points', 'photo_url', )


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    # players = serializers.HyperlinkedRelatedField(
    #     view_name='player_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Team
        fields = ('name', 'location', 'conference',
                  'wins', 'losses', 'photo_url',)
