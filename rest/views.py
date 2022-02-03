from rest_framework import generics
from .serializers import leagueSerializer, TeamSerializer, PlayerSerializer
from .models import League, Team, Player

# Create your views here.


class leagueList(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = leagueSerializer


class leagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = leagueSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
