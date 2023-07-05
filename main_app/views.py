from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Team, Players
from django.views.generic import DetailView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'


class TeamsList(TemplateView):
    template_name = "teams_list.html"

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["teams"] = Team.objects.filter(name__icontains=name)
            context["header"] = f"{name.upper()}"
        else:
            context["teams"] = Team.objects.all()
            context["header"] = "NFL Teams"
        return context
    
class TeamDetail(DetailView):
    model = Team
    template_name = "team_detail.html"


class PlayerCreate(View):

    def post(self, request, pk):
        playername = request.POST.get("playername")
        postion = request.POST.get("postion")
        points = request.POST.get("points")
        team = Team.objects.get(pk=pk)
        Players.objects.create(playername=playername, postion=postion, points=points, team=team)
        return redirect('team_detail', pk=pk)