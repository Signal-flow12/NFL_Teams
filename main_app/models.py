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

