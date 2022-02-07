from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    established = models.CharField(max_length=50)
    number_of_players = models.TextField()
    
    def __str__(self):
      return self.name
class Player(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
  name = models.CharField(max_length=50)
  age = models.CharField(max_length=10, default="Not Given")

  def __str__(self):
    return self.name