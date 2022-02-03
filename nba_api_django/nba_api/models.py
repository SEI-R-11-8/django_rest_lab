from django.db import models

# Create your models here.


class Conference(models.Model):
    CONFERENCE_CHOICES = (
        ('E', 'Eastern'),
        ('W', 'Western'),
    )
    name = models.CharField(max_length=1, choices=CONFERENCE_CHOICES)

    def __str__(self):
        return self.name


class Team(models.Model):
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    wins = models.IntegerField()
    losses = models.IntegerField
    conf_championships = models.IntegerField()
    nba_championships = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
