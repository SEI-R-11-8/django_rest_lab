from django.db import models

# Create your models here.








class Conference(models.Model):
  name = models.TextField()
  
  def __str__(self):
    return self.name

class Team(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100, default="location unavailable")
  number_of_wins = models.PositiveSmallIntegerField(default=0)
  number_of_loses = models.PositiveSmallIntegerField( default=0)
  conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='conferences')
  

  def __str__(self):
    return self.name

class Player(models.Model):
  name = models.TextField()
  position = models.TextField()
  age = models.PositiveSmallIntegerField(default=18)
  available_for_draft = models.BooleanField(default=True)
  teams = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teams')

  def __str__(self):
    return self.name
