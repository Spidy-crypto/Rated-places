from django.db import models

# Create your models here.

class addToFav(models.Model):
    name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100)