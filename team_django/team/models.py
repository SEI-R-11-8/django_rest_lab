from django.db import models

# Create your models here
# Artist=team
# Song=player


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mascot = models.TextField()

    def __str__(self):
        return self.name
