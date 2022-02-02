from django.db import models

# Create your models here.


class Conference(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100, default='unknown')
    city = models.CharField(max_length=100)
    abbr = models.CharField(max_length=3)
    wins = models.IntegerField(default=10)
    losses = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=25, default='Guard')
    age = models.IntegerField(default=25)
    ir = models.BooleanField(default=False)
    height = models.CharField(max_length=100)
    img = models.TextField(null=True)

    def __str__(self):
        return self.name
