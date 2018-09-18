from django.contrib import admin
from .models import RentalTrends

# Register your models here.

class RentalTrendsAdmin(admin.ModelAdmin):
    list_display = ['mostPopularVehicle','mostPopularType','mostPopularMonth']

admin.site.register(RentalTrends,RentalTrendsAdmin)
