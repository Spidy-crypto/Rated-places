from django.db import models

class addToFav(models.Model):
    name = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100)