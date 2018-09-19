from django.contrib import admin
from .models import RentalTrends
from .models import StoreTrends

# Register your models here.

class RentalTrendsAdmin(admin.ModelAdmin):
    list_display = ['mostPopularVehicle','mostPopularType','mostPopularMonth']

admin.site.register(RentalTrends, RentalTrendsAdmin)

class StoreTrendsAdmin(admin.ModelAdmin):
    list_display = ['storeID', 'storeProductivity', 'mostProductiveMonth', 'mostRentedVehicle',
                    'mostPickupOrReturn']

admin.site.register(StoreTrends, StoreTrendsAdmin)