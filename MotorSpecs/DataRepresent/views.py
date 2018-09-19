from django.shortcuts import render
from index.models import RentalTrends
from index.models import StoreTrends
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def rentaltrends(request):
    items = RentalTrends.objects.all()
    res = []
    for item in items:
        json = {
            'mostPopularVehicle': str(item.mostPopularVehicle),
            'mostPopularType': item.mostPopularType,
            'mostPopularMonth': item.mostPopularMonth,
        }
        res.append(json)    
    return render(request, 'rentaltrends.html', {'item_list': res})

@login_required
def storetrends(request):
    stores = StoreTrends.objects.all()
    res = []
    for store in stores:
        json = {
            'storeID':str(store.storeID),
            'storeProductivity':store.storeProductivity,
            'mostProductiveMonth':store.mostProductiveMonth,
            'mostRentedVehicle':store.mostRentedVehicle,
            'mostPickupOrReturn':store.mostPickupOrReturn
        }
        res.append(json)
    return render(request, 'storetrends.html', {'store_list':res})
