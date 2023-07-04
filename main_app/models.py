from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=150)
    img = models.CharField(max_length=300)
    conference = models.CharField(max_length=25)
    superbowlwins = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']