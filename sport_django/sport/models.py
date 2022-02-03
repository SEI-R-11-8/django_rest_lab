from django.db import models

# Create your models here.
#Name, Location, Conference, Wins, Losses - Team
# player- name, position, age, Injured Reserved list, 

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    wins = models.CharField(max_length=100)
    losses = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    injured_reserve_list = models.BooleanField()

    def __str__(self):
        return self.name