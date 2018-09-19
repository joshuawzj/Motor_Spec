from django.shortcuts import render
from index.models import RentalTrends
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
    return render(request, 'rentaltrends.html',{'item_list': res})
