# tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.leagueList.as_view(), name='league_list'),
    path('leagues/<int:pk>', views.leagueDetail.as_view(),
         name='league_detail'),
    path('teams/', views.TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),
    path('players/', views.PlayerList.as_view(), name='player_list'),
    path('players/<int:pk>', views.PlayerDetail.as_view(), name='player_detail')
]
