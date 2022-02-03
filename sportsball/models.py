from django.db import models

# Create your models here.
class Conference(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class Team(models.Model):
  conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='teams')
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  wins = models.IntegerField()
  losses = models.IntegerField()

  def __str__(self):
    return self.name

class Player(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  position = models.CharField(max_length=100)
  injured = models.BooleanField(default=False)

  def __str__(self):
    return self.name