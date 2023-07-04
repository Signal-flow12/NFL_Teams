from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('teams/', views.TeamsList.as_view(), name='teams_list'),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name="team_detail"),
]