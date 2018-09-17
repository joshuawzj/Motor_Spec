from django.contrib import admin
from .models import VehicleList

# Register your models here.


class VehicleListAdmin(admin.ModelAdmin):
    list_display = ['carID','carMakeName','carModel','carSeries','carSeriesYear','carPriceNew','carEngineSize',
                    'carFuelSystem','carTankCapacity','carPower','carSeatingCapacity','carStandardTransmission',
                    'carBodyType','carDrive','carWheelbase'
                    ]

admin.site.register(VehicleList,VehicleListAdmin)
