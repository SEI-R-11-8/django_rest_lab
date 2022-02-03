from django.db import models

# Create your models here.


class Conference(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Team(models.Model):
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    championships = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
      Team, on_delete=models.CASCADE, related_name='players'
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=40)
    age = models.IntegerField()
    height = models.CharField(max_length=10)
    image_url = models.TextField()
    all_star_selections = models.IntegerField(default=0)

    def __str__(self):
      return self.name