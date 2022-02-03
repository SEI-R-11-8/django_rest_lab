from rest_framework import serializers
from .models import Player, Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Team
        fields = ('id', 'name', 'location', 'conference',
                  'wins', 'losses', 'players')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        # don't need 'many' because only one team to a player
        read_only=True
    )

    class Meta:
        model = Player
        fields = ('id', 'team', 'team_id', 'name',
                  'position', 'age', 'injured_list')
