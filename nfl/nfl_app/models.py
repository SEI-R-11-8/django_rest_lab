from django.db import models

# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Player(models.Model):
    position_choices = [
        ('Offense', (
            ('O_QB', 'Quarterback'),
            ('O_RB', 'Running Back'),
            ('O_FB', 'Fullback'),
            ('O_WR', 'Wide Receiver'),
            ('O_TE', 'Tight End'),
            ('O_OT', 'Offensive Tackle'),
            ('O_OG', 'Offensive Guard'),
            ('O_C', 'Center')
        )),
        ('Defense', (
            ('D_NT', 'Nose Tackle'),
            ('D_DT', 'Defensive Tackle'),
            ('D_DE', 'Defensive End'),
            ('D_LB', 'Linebacker'),
            ('D_CB', 'Cornerback'),
            ('D_FS', 'Free Safety'),
            ('D_SS', 'Strong Safety')
        )),
        ('Special', (
            ('S_K', 'Kicker'),
            ('S_P', 'Punter'),
            ('S_LS', 'Long Snapper'),
            ('S_H', 'Holder'),
            ('S_KR', 'Kick Returner'),
            ('S_PR', 'Punt Returner')
        ))
    ]
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=4, choices=position_choices)
    age = models.IntegerField()
    injured_reserve = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name