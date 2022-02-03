from django.db import models

# Create your models here
# Artist=team, team fields should be: name, location and conference
# Song=player
# create player model: fields for player should be: name, position, age, variable on whether or not injured reserved list (boolean?) and "any other stats you think are relevant"
# player belongs to Team
# teams have many players
# create ForeignKey for player class


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mascot = models.TextField()
    special_moves = models.TextField(default='none')

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100, default='name unknown')
    position = models.CharField(max_length=100, default='position unknown')
    is_deatheater = models.BooleanField(default=False)

    def __str__(self):
        return self.name
