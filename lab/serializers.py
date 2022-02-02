from rest_framework import serializers
from .models import Player, Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='team_detail'
    )

    class Meta:
        model = Team
        fields = ('id', 'name', 'location', 'conference', 'wins',  'losses', 'team_url',
                  'player',)


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
        fields = ('id', 'team', 'team_id', 'name',
                  'position', 'age', 'Reserved_list',)
