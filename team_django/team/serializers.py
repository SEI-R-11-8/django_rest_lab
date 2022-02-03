from urllib.request import AbstractDigestAuthHandler
from rest_framework import serializers
from .models import Team, Player


class TeamSerializer(serializers.HyperLinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Team
        fields = ('id', 'name', 'country', 'mascot', 'special_moves',)


class PlayerSerializer(serializers.HyperLinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail', read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'name', 'position', 'is_deatheater')
