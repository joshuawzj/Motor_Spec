from django.shortcuts import render
from index.models import VehicleList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from .models import VehicleList
import json

# Create your views here.

def index(request):
    cars = VehicleList.objects.all()
    res = []
    for car in cars:
        json = {
            'carID':str(car.carID),
            'carMakeName':car.carMakeName,
            'carModel':car.carModel,
            'carSeries':car.carSeries,
            'carSeriesYear':car.carSeriesYear,
            'carPriceNew':car.carPriceNew,
            'carEngineSize':car.carEngineSize,
            'carFuelSystem':car.carFuelSystem,
            'carTankCapacity':car.carTankCapacity,
            'carPower':car.carPower,
            'carSeatingCapacity':car.carSeatingCapacity,
            'carStandardTransmission':car.carStandardTransmission,
            'carBodyType':car.carBodyType,
            'carDrive':car.carDrive,
            'carWheelbase':car.carWheelbase
        }
        print(json)
        res.append(json)

    paginator = Paginator(res, 15)
    page = request.GET.get('page','1')
    try:
        res = paginator.page(page)
    except PageNotAnInteger:
        res = paginator.page(1)
    except EmptyPage:
        res = paginator.page(paginator.num_pages)



    return render(request, 'vehiclelist.html',{'car_list':res})

