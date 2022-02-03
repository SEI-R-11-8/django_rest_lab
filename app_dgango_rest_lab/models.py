from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    number_of_wins = models.IntegerField(max_length=100)
    number_of_losses = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    injured_reserved_list = models.TextField(blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="player")

    def __str__(self):
        return self.name