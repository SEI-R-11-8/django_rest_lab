from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Team, Player
from .forms import TeamForm, PlayerForm
# Create your views here.

############# get
def team_list(req):
    teams = Team.objects.all().order_by('name')
    return render(req, 'la_liga/team_list.html', {'teams': teams})

def player_list(req):
    players = Player.objects.all().order_by('name')
    return render(req, 'la_liga/player_list.html', {'players': players})

def team_details(req, pk):
    team = Team.objects.get(id=pk)
    return render(req, 'la_liga/team_details.html', {'team': team})

def player_details(req, pk):
    player = Player.objects.get(id=pk)
    return render(req, 'la_liga/player_details.html', {'player': player})

############## post
def team_create(req):
    if req.method == 'POST':
        form = TeamForm(req.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('team_details', pk=decade.pk)
    else:
        form = TeamForm()
    return render(req, 'la_liga/team_form.html', {'form': form})

def player_create(req):
    if req.method == 'POST':
        form = PlayerForm(req.POST)
        if form.is_valid():
            player = form.save()
            return redirect('player_details', pk=player.pk)
    else:
        form = PlayerForm()
    return render(req, 'la_liga/fad_form.html', {'form': form}) 

########### edit
def decade_edit(req, pk):
    decade = Team.objects.get(pk=pk)
    if req.method == "POST":
        form = TeamForm(req.POST, instance=decade)
        if form.is_valid():
            team = form.save()
            return redirect('team_details', pk=team.pk)
    else:
        form = TeamForm(instance=decade)
    return render(req, 'la_liga/team_form.html', {'form': form})

def player_edit(req, pk):
    fad = Player.objects.get(pk=pk)
    if req.method == "POST":
        form = PlayerForm(req.POST, instance=fad)
        if form.is_valid():
            player = form.save()
            return redirect('player_details', pk=player.pk)
    else:
        form = PlayerForm(instance=fad)
    return render(req, 'la_liga/fad_form.html', {'form': form})


######## delete
def team_delete(req, pk):
    Team.objects.get(id=pk).delete()
    return redirect('team_list')

def player_delete(req, pk):
    Player.objects.get(id=pk).delete()
    return redirect('player_list') 