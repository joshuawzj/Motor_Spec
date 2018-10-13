from django.contrib import admin
from .models import User,VehicleList, RentalHistory, CustomerDetails, RentalTrends, StoreTrends, StoreDetail

# Register your models here.
admin.site.register(User)
admin.site.register(VehicleList)
admin.site.register(RentalHistory)
admin.site.register(CustomerDetails)
admin.site.register(RentalTrends)
admin.site.register(StoreTrends)
admin.site.register(StoreDetail)

