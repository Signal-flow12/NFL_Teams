from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 

# Create your views here.
class Home(View):
    def get(self, req):
        return HttpResponse('Hello world!')
    
class About(View):
    def get(self, req):
        return HttpResponse('This is my about')