from rest_framework import serializers
from .models import Conference, Team, Player

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
  teams = serializers.HyperlinkedRelatedField(
    view_name='team_detail',
    many=True,
    read_only=True
  )

  conference_url = serializers.ModelSerializer.serializer_url_field(
    view_name='conference_detail'
  )

  class Meta:
    model = Conference
    fields = ('id', 'name', 'teams', 'conference_url')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
  players = serializers.HyperlinkedRelatedField(
    view_name='player_detail',
    many=True,
    read_only=True
  )

  conference = serializers.HyperlinkedRelatedField(
    view_name='conference_detail',
    read_only=True
  )

  conference_id = serializers.PrimaryKeyRelatedField(
    queryset=Conference.objects.all(),
    source='conference'
  )

  class Meta:
    model = Team
    fields = ('id', 'name', 'location', 'wins', 'losses', 'conference', 'players', 'conference_id')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  team = serializers.HyperlinkedRelatedField(
    view_name='team_detail',
    read_only=True
  )

  team_id = serializers.PrimaryKeyRelatedField(
    queryset=Team.objects.all(),
    source='team'
  )

  class Meta:
    model = Player
    fields = ('id', 'name', 'age', 'position', 'injured', 'team', 'team_id')