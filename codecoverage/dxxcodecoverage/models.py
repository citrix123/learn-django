from django.db import models

# Create your models here.

class Album(models.Model):
    """docstring for Album."""
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
