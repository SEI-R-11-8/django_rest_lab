from django.shortcuts import render
from nfl_app.serializers import ConferenceSerializer
from rest_framework import generics
from .models import Conference, Team, Player
from .serializers import ConferenceSerializer, TeamSerializer, PlayerSerializer

# Create your views here.
class ConferenceList(generics.ListCreateAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

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
    seriazlier_class = PlayerSerializer