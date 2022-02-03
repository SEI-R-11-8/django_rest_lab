from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.

from .models import Team, Player
from .forms import TeamForm, PlayerForm

from rest_framework import generics
from .serializers import TeamSerializer, PlayerSerializer

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