from django.shortcuts import render
from index.models import RentalTrends

# Create your views here.


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
    return render(request, 'rentaltrends.html',{'item_list': res})