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
        fields = ('area', 'conference_url', 'teams',)


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    conference = serializers.HyperlinkedRelatedField(
        view_name='conference_detail',
        read_only=True
    )

    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    conference_id = serializers.PrimaryKeyRelatedField(
        queryset=Conference.objects.all(),
        source='conference'
    )

    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='team_detail'
    )

    class Meta:
        model = Team
        fields = ('name', 'location', 'season_wins',
                  'season_losses', 'conference', 'conference_id', 'team_url', 'players')


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
