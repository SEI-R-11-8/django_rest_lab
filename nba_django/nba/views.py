from rest_framework import generics
from .serializers import PlayerSerializer, TeamSerializer
from .models import Players, Team


class PlayerList(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# from django.shortcuts import render
# redirect
# from .forms import PlayerForm, TeamForm
# from .models import Team, Players


# def player_list(request):
#     players = Players.objects.all()
#     return render(request, 'nba/player_list.html', {'players': players})


# def player_detail(request, pk):
#     player = Players.objects.get(id=pk)
#     return render(request, 'nba/player_detail.html', {'player': player})


# def team_list(request):
#     teams = Team.objects.all()
#     return render(request, 'nba/team_list.html', {'teams': teams})


# def team_detail(request, pk):
#     team = Team.objects.get(id=pk)
#     return render(request, 'nba/team_detail.html', {'team': team})


# def player_create(request):
#     if request.method == 'POST':
#         form = PlayerForm(request.POST)
#         if form.is_valid():
#             player = form.save()
#             return redirect('player_detail', pk=player.pk)
#     else:
#         form = PlayerForm()
#     return render(request, 'nba/player_form.html', {'form': form})


# def team_create(request):
#     if request.method == 'POST':
#         form = TeamForm(request.POST)
#         if form.is_valid():
#             team = form.save()
#             return redirect('team_detail', pk=team.pk)
#     else:
#         form = TeamForm()
#     return render(request, 'nba/team_form.html', {'form': form})


# def player_edit(request, pk):
#     player = Players.objects.get(pk=pk)
#     if request.method == "POST":
#         form = PlayerForm(request.POST, instance=player)
#         if form.is_valid():
#             player = form.save()
#             return redirect('player_detail', pk=player.pk)
#     else:
#         form = PlayerForm(instance=player)
#     return render(request, 'nba/player_form.html', {'form': form})


# def team_edit(request, pk):
#     team = Team.objects.get(pk=pk)
#     if request.method == "POST":
#         form = TeamForm(request.POST, instance=team)
#         if form.is_valid():
#             team = form.save()
#             return redirect('team_detail', pk=team.pk)
#     else:
#         form = TeamForm(instance=team)
#     return render(request, 'nba/team_form.html', {'form': form})


# def player_delete(request, pk):
#     Players.objects.get(id=pk).delete()
#     return redirect('player_list')


# def team_delete(request, pk):
#     Team.objects.get(id=pk).delete()
#     return redirect('team_list')
