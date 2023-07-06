from django.db import models
# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=150)
    img = models.CharField(max_length=300)
    conference = models.CharField(max_length=30)
    superbowlwins = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']



class Players(models.Model):

    playername = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    points = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.playername
    
class Fantasy_Team(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    players = models.ManyToManyField(Players)

    def __str__(self):
        return self.title



