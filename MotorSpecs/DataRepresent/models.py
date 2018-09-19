from django.db import models

# Create your models here.

class RentalTrends(models.Model):
    mostPopularVehicle = models.CharField(max_length=50)
    mostPopularType = models.CharField(max_length=50)
    mostPopularMonth = models.CharField(max_length=50)
    def __str__(self):
        return self.mostPopularVehicle + ', ' + self.mostPopularType + ', ' + self.mostPopularMonth



class StoreTrends(models.Model):
    storeID = models.CharField(max_length=250)
    storeProductivity = models.CharField(max_length=50)
    mostProductiveMonth = models.CharField(max_length=50)
    mostRentedVehicle = models.CharField(max_length=50)
    mostPickupOrReturn = models.CharField(max_length=10)
    def __str__(self):
        return self.storeID + ' - ' + self.storeProductivity + ', ' + self.mostRentedVehicle + ', ' + self.mostPickupOrReturn + ', ' + self.mostProductiveMonth
