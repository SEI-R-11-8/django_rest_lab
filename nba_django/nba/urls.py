from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('', views.player_list, name='player_list'),
    # path('teams/', views.team_list, name='team_list'),
    # path('players/<int:pk>', views.player_list, name='player_list'),
    path('players/', views.PlayerList.as_view(), name='player_list'),
    # path('players/<int:pk>', views.player_detail.as_view(), name='player_detail'),
    # path('teams/', views.team_list.as_view(), name="team_list"),
    # path('teams/<int:pk>', views.team_detail.as_view(), name="team_detail")
]
