from django.db import models

# Create your models here.

class RentalTrends(models.Model):
    mostPopularVehicle = models.CharField(max_length=50)
    mostPopularType = models.CharField(max_length=50)
    mostPopularMonth = models.CharField(max_length=50)
    def __str__(self):
        return self.mostPopularVehicle + ', ' + self.mostPopularType + ', ' + self.mostPopularMonth