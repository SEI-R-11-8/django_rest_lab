from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    established = models.CharField(max_length=50)
    number_of_players = models.TextField()
    


    def __str__(self):
      return self.name
