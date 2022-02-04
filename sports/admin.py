from django.contrib import admin

# Register your models here.

from .models import Team, Player, Conference

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Conference)