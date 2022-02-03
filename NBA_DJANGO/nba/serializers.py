from rest_framework import serializers
from .models import Conference, Team, Player


class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Conference
        fields = ('id', 'name', 'teams')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        read_only=True,
        many=True

    )

    class Meta:
        model = Team
        fields = ('id', 'name', 'players', 'city',
                  'championships')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )

    class Meta:
        model = Player
        fields = ('id', 'name', 'position',
                  'age', 'height', 'image_url', 'all_star_selections' ,'team')