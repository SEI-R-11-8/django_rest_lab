from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    conference = models.TextField(max_length=100)
    num_wins = models.CharField(max_length=100)
    num_losses = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100, default='no player name')
    posistion = models.CharField(max_length=100, default='no posistion')
    age = models.CharField(max_length=100, null=True)
    is_injured = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name