from rest_framework import serializers
from .models import Player, Team, Conference

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
      view_name='team_detail',
      read_only=True
    )
    teams_id = serializers.PrimaryKeyRelatedField(
      queryset=Team.objects.all(),
      source='teams'
    )
    class Meta:
      model = Player 
      fields = ('id', 'teams', 'teams_id', 'name',  'position', 'age', 'available_for_draft', )

class TeamSerializer(serializers.HyperlinkedModelSerializer):
  conference_url = serializers.ModelSerializer.serializer_url_field(
    view_name='conference_detail',
  )
  player = serializers.HyperlinkedRelatedField(
    view_name = 'player_detail',
    read_only = True,
  )  
  conference_id = serializers.PrimaryKeyRelatedField(
    queryset=Conference.objects.all(),
    source='conference'
    )
  class Meta:
    model = Team
    fields = ('id', 'conference_id', 'conference_url', 'name','number_of_wins', 'number_of_loses', 'location', 'player',)

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
  teams = serializers.HyperlinkedRelatedField(
    view_name="team_detail",
    read_only=True,
  )
  conference_url = serializers.ModelSerializer.serializer_url_field(
    view_name='conference_detail'
    )
  class Meta:
    model = Conference
    fields = ('id', 'conference_url', 'name', 'teams', )