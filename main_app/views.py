from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'

class  Teams:
    def __init__(self, name, image, conference):
        self.name = name
        self.image = image
        self.conference = conference

teams = [
    Teams("Raiders", "https://pbs.twimg.com/profile_images/1611220466743783429/gg0OPgEw_400x400.jpg", "AFC"),
    Teams("Eagles", "https://1000logos.net/wp-content/uploads/2017/05/Philadelphia-Eagles-Logo.png", "NFC"),
    Teams("Giants", "https://s.yimg.com/cv/apiv2/default/nfl/20190724/500x500/2019_NYG_wbg.png", "NFC")
]

class TeamsList(TemplateView):
    template_name = "teams_list.html"

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = teams
        return context