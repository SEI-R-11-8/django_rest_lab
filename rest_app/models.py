from django.db import models

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='team')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo_url = models.TextField(default= 'no logo')

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player')
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    photo_url = models.TextField(default='no photo')

    def __str__(self):
        return self.name
