from django.db import models

# Create your models here.

class VehicleList(models.Model):
    carID = models.CharField(max_length=10)
    carMakeName = models.CharField(max_length=50)
    carModel = models.CharField(max_length=50)
    carSeries = models.CharField(max_length=50)
    carSeriesYear = models.CharField(max_length=10)
    carPriceNew = models.CharField(max_length=15)
    carEngineSize = models.CharField(max_length=10)
    carFuelSystem = models.CharField(max_length=50)
    carTankCapacity = models.CharField(max_length=10)
    carPower = models.CharField(max_length=10)
    carSeatingCapacity = models.CharField(max_length=5)
    carStandardTransmission = models.CharField(max_length=10)
    carBodyType = models.CharField(max_length=50)
    carDrive = models.CharField(max_length=10)
    carWheelbase = models.CharField(max_length=10)
    def __str__(self):
        return self.carID + ' - ' + self.carMakeName