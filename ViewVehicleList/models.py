from django.db import models


# Create your models here.

class Vehicle(models.Model):
    CarBrand = models.CharField(max_length=32, default='Car Brand')
    CarModel = models.CharField(max_length=32, default='Model')


