from django.db import models

# Create your models here.
class Team(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  league = models.CharField(max_length=100)
  wins = models.IntegerField()
  losses = models.IntegerField()

  def __str__(self):
    return self.name

class Player(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
  name = models.CharField(max_length=200)
  position = models.CharField(max_length=100)
  age = models.IntegerField()
  injured_list = models.BooleanField()

  def __str__(self):
    return self.name
