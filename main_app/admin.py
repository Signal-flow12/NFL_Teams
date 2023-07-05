from django.contrib import admin
from .models import Team, Players, Fantasy_Team

# Register your models here.
admin.site.register(Team)
admin.site.register(Players)
admin.site.register(Fantasy_Team)
