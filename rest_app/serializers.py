from rest_framework import serializers
from .models import League, Team, Player

class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        many=True,
        read_only=True
    )
    league_url = serializers.ModelSerializer.serializer_url_field(
        view_name='league_detail'
    )
    class Meta:
       model = League 
       fields = ('id', 'league_url','nationality', 'name','team',)

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    league = serializers.HyperlinkedRelatedField(
        view_name='league_detail',
        read_only=True
    )
    league_id = serializers.PrimaryKeyRelatedField(
        queryset=League.objects.all(),
        source='league'
    )
    player = serializers.HyperlinkedRelatedField(
        view_name='players_detail',
        many=True,
        read_only=True
    )
 

    class Meta:
        model = Team
        fields = ('id', 'league','league_id', 'name', 'logo_url', 'location','player')

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
        fields = ('id', 'team','team_id', 'name', 'photo_url', 'age')