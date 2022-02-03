from django.db import models

# Create your models here.

class Team(models.Model):
  name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  conference=models.CharField(max_length=100)
  wins=models.IntegerField()
  losses=models.IntegerField()

  def __str__(self):
    return self.name

class Player(models.Model):
  name=models.CharField(max_length=100)
  position=models.CharField(max_length=100)
  age=models.IntegerField()
  injured=models.BooleanField()
  team=models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

  def __str__(self):
    return self.name
