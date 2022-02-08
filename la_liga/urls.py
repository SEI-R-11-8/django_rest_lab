from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('team/<int:pk>', views.team_details, name='team_details'),
    path('team/new', views.team_create, name='team_create'),
    path('team/<int:pk>/edit', views.decade_edit, name='decade_edit'),
    path('team/<int:pk>/delete', views.team_delete, name='team_delete'),

    path('player/', views.player_list, name='player_list'),
    path('player/<int:pk>', views.player_details, name='player_details'),
    path('player/new', views.player_create, name='player_create'),
    path('player/<int:pk>/edit', views.player_edit, name='player_edit'),
    path('player/<int:pk>/delete', views.player_delete, name='player_delete')
] 