from tkinter import CASCADE
from django.db import models

# Create your models here.
class League(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Division(models.Model):
  league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='divisions')
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Team(models.Model):
  league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
  division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='teams')
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  wins = models.PositiveSmallIntegerField()
  losses = models.PositiveSmallIntegerField()
  website = models.TextField()

  def __str__(self):
    return self.name

class Player(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
  name = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  age = models.PositiveSmallIntegerField()
  ir_list = models.BooleanField()
  war = models.FloatField()

  def __str__(self):
    return self.name