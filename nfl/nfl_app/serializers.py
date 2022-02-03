from rest_framework import serializers
from .models import Conference, Team, Player

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name = 'team_detail',
        many = True,
        read_only = True
    )
    conference_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'conference_detail'
    )
    class Meta:
        model = Conference
        fields = ('id', 'name', 'teams', 'conference_url', 'created_at', 'updated_at')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        view_name = 'player_detail',
        many = True,
        read_only = True
    )
    conference = serializers.HyperlinkedRelatedField(
        view_name = 'conference_detail',
        read_only = True
    )
    conference_id = serializers.PrimaryKeyRelatedField(
        queryset = Conference.objects.all(),
        source = 'conference'
    )
    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'team_detail'
    )
    class Meta:
        model = Team
        fields = (
            'id', 
            'name', 
            'location', 
            'wins', 
            'losses', 
            'players',
            'conference', 
            'conference_id', 
            'team_url', 
            'created_at', 
            'updated_at'
        )

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name = 'team_detail',
        read_only = True
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset = Team.objects.all(),
        source = 'team'
    )
    class Meta:
        model = Player
        fields = (
            'id',
            'position',
            'age',
            'injured_reserve',
            'team',
            'team_id',
            'created_at',
            'updated_at'
        )