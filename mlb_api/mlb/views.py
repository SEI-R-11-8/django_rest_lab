from ast import Div
from rest_framework import generics
from .serializers import LeagueSerializer, DivisionSerializer, TeamSerializer, PlayerSerializer
from .models import League, Division, Team, Player

class LeagueList(generics.ListCreateAPIView):
  queryset = League.objects.all().order_by('id')
  serializer_class = LeagueSerializer

class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = League.objects.all()
  serializer_class = LeagueSerializer

class DivisionList(generics.ListCreateAPIView):
  queryset = Division.objects.all().order_by('id')
  serializer_class = DivisionSerializer

class DivisionDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Division.objects.all()
  serializer_class = DivisionSerializer

class TeamList(generics.ListCreateAPIView):
  queryset = Team.objects.all().order_by('name')
  serializer_class = TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

class PlayerList(generics.ListCreateAPIView):
  queryset = Player.objects.all().order_by('name')
  serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer