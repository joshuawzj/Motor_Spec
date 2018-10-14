from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=50)
    def __str__(self):
        return self.userName + ', ' + self.userPassword

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

class RentalHistory(models.Model):
    storeID = models.CharField(max_length=5)
    storeName = models.CharField(max_length=100)
    orderID = models.CharField(max_length=10)
    orderCreationDate = models.CharField(max_length=25)
    orderPickupOrReturn = models.CharField(max_length=10)
    orderPickupOrReturnDate = models.CharField(max_length=250)
    customerID = models.CharField(max_length=10)
    customerName = models.CharField(max_length=50)
    carID = models.CharField(max_length=10)
    carMakeName = models.CharField(max_length=50)
    def __str__(self):
        return self.storeName + ' - ' + self.orderID

class CustomerDetails(models.Model):
    customerID = models.CharField(max_length=10)
    customerName = models.CharField(max_length=50)
    customerPhone = models.CharField(max_length=50)
    customerAddress = models.CharField(max_length=75)
    customerDOB = models.CharField(max_length=15)
    customerGender = models.CharField(max_length=10)
    customerOccupation = models.CharField(max_length=50)
    def __str__(self):
        return self.customerID + ' - ' + self.customerName

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

class StoreDetail(models.Model):
    storeID = models.CharField(max_length=250)
    storeName = models.CharField(max_length=250)
    storeAddress = models.CharField(max_length=75)
    storePhone = models.CharField(max_length=50)
    storeCity = models.CharField(max_length=75)
    storeStateName = models.CharField(max_length=75)
    def __str__(self):
        return self.storeName + ' - ' + self.storeID

