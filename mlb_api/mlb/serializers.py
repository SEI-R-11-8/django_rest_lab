from ast import Div
from rest_framework import serializers
from .models import League, Division, Team, Player

class LeagueSerializer(serializers.HyperlinkedModelSerializer):
  divisions = serializers.HyperlinkedRelatedField(
    view_name = 'division_detail',
    many = True,
    read_only = True
  )

  teams = serializers.HyperlinkedRelatedField(
    view_name = 'team_detail',
    many = True,
    read_only = True
  )

  league_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'league_detail'
  )

  class Meta:
    model = League
    fields = ('id', 'name', 'league_url', 'divisions', 'teams')

class DivisionSerializer(serializers.HyperlinkedModelSerializer):
  league = serializers.HyperlinkedRelatedField(
    view_name = 'league_detail',
    read_only = True
  )

  league_id = serializers.PrimaryKeyRelatedField(
    queryset = League.objects.all(),
    source = 'league'
  )

  teams = serializers.HyperlinkedRelatedField(
    view_name = 'team_detail',
    many = True,
    read_only = True
  )

  division_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'division_detail'
  )

  class Meta:
    model = Division
    fields = ('id', 'name', 'division_url', 'league', 'league_id', 'teams')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
  league = serializers.HyperlinkedRelatedField(
    view_name = 'league_detail',
    read_only = True
  )

  league_id = serializers.PrimaryKeyRelatedField(
    queryset = League.objects.all(),
    source = 'league'
  )

  division = serializers.HyperlinkedRelatedField(
    view_name = 'division_detail',
    read_only = True
  )

  division_id = serializers.PrimaryKeyRelatedField(
    queryset = Division.objects.all().order_by('id'),
    source = 'division'
  )

  players = serializers.HyperlinkedRelatedField(
    view_name = 'player_detail',
    many = True,
    read_only = True
  )

  team_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'team_detail'
  )

  class Meta:
    model = Team
    fields = ('id', 'name', 'team_url', 'location', 'wins', 'losses', 'website', 'league', 'league_id', 'division', 'division_id', 'players')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  team = serializers.HyperlinkedRelatedField(
    view_name = 'team_detail',
    read_only = True
  )

  team_id = serializers.PrimaryKeyRelatedField(
    queryset = Team.objects.all().order_by('name'),
    source = 'team'
  )

  player_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'player_detail'
  )

  class Meta:
    model = Player
    fields = ('id', 'name', 'player_url', 'team', 'team_id', 'position', 'age', 'ir_list', 'war')