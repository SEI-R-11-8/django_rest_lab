from rest_framework import serializers
from .models import League, Team, Player


class leagueSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        many=True,
        read_only=True
    )

    league_url = serializers.ModelSerializer.serializer_url_field(
        view_name='league_detail'
    )

    class Meta:
        model = League
        fields = ('area', 'league_url', 'teams',)


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    league = serializers.HyperlinkedRelatedField(
        view_name='league_detail',
        read_only=True
    )

    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    league_id = serializers.PrimaryKeyRelatedField(
        queryset=League.objects.all(),
        source='league'
    )

    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='team_detail'
    )

    class Meta:
        model = Team
        fields = ('name', 'location', 'season_wins',
                  'season_losses', 'league', 'league_id', 'team_url', 'players')


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
        fields = ('name', 'position', 'age',
                  'is_on_injured_list', 'team', 'team_id')
