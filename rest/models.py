from django.db import models

# Create your models here.


class League(models.Model):
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.area


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    season_wins = models.IntegerField()
    season_losses = models.IntegerField()
    league = models.ForeignKey(
        League, on_delete=models.CASCADE, related_name='teams'
    )

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    is_on_injured_list = models.BooleanField()
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')
