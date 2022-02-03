from rest_framework import serializers
from .models import Team, Player


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Team
        fields = ('id', 'players', 'name', 'location', 'wins', 'league', 'losses')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'name', 'position', 'age', 'injured_list', 'team_id')
