from django.shortcuts import render
from index.models import RentalTrends
<<<<<<< HEAD
<<<<<<< HEAD
from index.models import StoreTrends
=======
from django.contrib.auth.decorators import login_required
>>>>>>> d9aa24a196fef12596d941551370c1f6cf9622e7
=======
from django.contrib.auth.decorators import login_required
>>>>>>> d9aa24a196fef12596d941551370c1f6cf9622e7

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
<<<<<<< HEAD
<<<<<<< HEAD
    return render(request, 'rentaltrends.html', {'item_list': res})


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
=======
    return render(request, 'rentaltrends.html',{'item_list': res})
>>>>>>> d9aa24a196fef12596d941551370c1f6cf9622e7
=======
    return render(request, 'rentaltrends.html',{'item_list': res})
>>>>>>> d9aa24a196fef12596d941551370c1f6cf9622e7
