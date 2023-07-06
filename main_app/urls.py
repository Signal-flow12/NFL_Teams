from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('new/', views.FantasyCreate.as_view(), name='fantasy_create'),
    path('about/', views.About.as_view(), name='about'),
    path('teams/', views.TeamsList.as_view(), name='teams_list'),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name="team_detail"),
    path('teams/<int:pk>/players/new', views.PlayerCreate.as_view(), name="player_create"),
    path('fantasy/<int:pk>/players/<int:players_pk>/', views.FantasyPlayerAssoc.as_view(), name="fantasy_player_assoc"),

]