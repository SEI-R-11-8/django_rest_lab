from rest_framework import serializers
from .models import Conference, Team, Player

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name='teams',
        many=True,
        read_only=True
    )
    class Meta:
       model = Artist 
       fields = ('id', 'name', 'teams' )