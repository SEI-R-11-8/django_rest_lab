from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    wins = models.IntegerField()
    losses = models.IntegerField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Players(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="players")
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    gp = models.CharField(max_length=100)
    injured_reserved = models.BooleanField(default=True)
    points = models.IntegerField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name
