from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Team 
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