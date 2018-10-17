from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.db.models import Q
from index.models import VehicleList, CustomerDetails, StoreDetail, RentalHistory, User
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    assert isinstance(request, HttpRequest)
    currentUser = request.user

    template = loader.get_template('WebApp/dashboard.html')
    context = {
        'currentUser': currentUser
    }
    return HttpResponse(template.render(context, request))

def home(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'WebApp/home.html')

def aboutUs(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'WebApp/aboutUs.html')

def LegalResources(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'WebApp/LegalResources.html')

def Stores(request):
    storeList = StoreDetail.objects.all

    template = loader.get_template('WebApp/stores.html')
    context = {
        'storeList': storeList
    }
    return HttpResponse(template.render(context, request))

# search_list listens to the user request for the search and displays website-wide content containing the keyword
def search_list(request):
    query = request.GET.get('search_box')
    vehicleList_results = None
    customerDetails_results = None

    if query:
        # TODO: if Staff/Customer statement here
        # Filtering search results
        vehicleList_results = VehicleList.objects.filter(
            Q(carID__iexact=query) |
            Q(carMakeName__iexact=query) |
            Q(carModel__iexact=query) |
            Q(carSeries__iexact=query) |
            Q(carFuelSystem__iexact=query) |
            Q(carStandardTransmission__iexact=query) |
            Q(carBodyType__iexact=query) |
            Q(carDrive__iexact=query)
        )
        customerDetails_results = CustomerDetails.objects.filter(
            Q(customerID__iexact=query) |
            Q(customerName__contains=query)
        )
        if vehicleList_results:
            all_results = vehicleList_results
        elif customerDetails_results:
            all_results = customerDetails_results
        else:
            all_results = None

    else:
        # TODO: if Staff/Customer statement here
        all_results = None

    if all_results != None:
        count = all_results.__len__()
    else:
        count = 0
    template = loader.get_template('WebApp/results.html')
    context = {
        'all_results': all_results,
        'vehicleList_results': vehicleList_results,
        'customerDetails_results': customerDetails_results,
        'search_count': count
    }
    return HttpResponse(template.render(context, request))

def CustomerSearch_list(request):
    query = request.GET.get('searchBox')
    vehicleList_results = None
    customerDetails_results = None

    if query:
        # TODO: if Staff/Customer statement here
        # Filtering search results
        vehicleList_results = VehicleList.objects.filter(
            Q(carID__contains=query) |
            Q(carMakeName__contains=query) |
            Q(carModel__contains=query) |
            Q(carSeries__contains=query) |
            Q(carFuelSystem__contains=query) |
            Q(carStandardTransmission__contains=query) |
            Q(carBodyType__contains=query) |
            Q(carDrive__contains=query)
        )
        all_results = vehicleList_results

    else:
        # TODO: if Staff/Customer statement here
        all_results = None

    if all_results != None:
        count = all_results.__len__()
    else:
        count = 0
    template = loader.get_template('WebApp/results.html')
    context = {
        'all_results': all_results,
        'vehicleList_results': vehicleList_results,
        'customerDetails_results': customerDetails_results,
        'search_count': count
    }
    return HttpResponse(template.render(context, request))

def vehicleRecommendation(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'WebApp/vehicleRecommendation.html')

# vehicleRecommendationResult() receives the user input for every car description. If an input exists, the vehicle
# database is filtered to produce a QuerySet of the given vehicles with a description which matches the user input.
# If an input is non-existent, the field is ignored and other fields are used to filter the database. If all fields
# are empty, every field is ignored, resulting in no results.
# The function also consists of a counter, counting the number of final results, which is passed on as search_count
# in the variable "context".
# Finally, the template is loaded and recommendationResults.html is loaded, using "context" to pass variables to the
# template.
def vehicleRecommendationResult(request):
    results = None

    carType = request.GET.get('car_box')                        # Car Type
    transmissionType = request.GET.get('transmission_box')      # Car Transmission Type
    engineSize = request.GET.get('engine_box')                  # Car Engine Size
    fuelType = request.GET.get('fuel_box')                      # Car Fuel Type
    year = request.GET.get('year_box')                          # Car Series Year
    model = request.GET.get('model_box')                        # Car Model

    # Checks if each field contains a user input
    if not carType:
        carType = True
    if not transmissionType:
        transmissionType = True
    if not engineSize:
        engineSize = True
    if not fuelType:
        fuelType = True
    if not year:
        year = True
    if not model:
        model = True

    # Filters the vehicle database using the user input
    results = VehicleList.objects.filter(
        Q(carBodyType__contains=carType) |
        Q(carStandardTransmission__contains=transmissionType) |
        Q(carEngineSize__contains=engineSize) |
        Q(carFuelSystem__contains=fuelType) |
        Q(carSeriesYear__contains=year) |
        Q(carModel__contains=model)
    )

    # Checks if results exist and counts the results
    if results != None:
        count = results.__len__()
    else:
        count = 0

    # Loads HTML into template and stores variables in context to prepare loading the page
    template = loader.get_template('WebApp/recommendationResults.html')
    context = {
        'results': results,
        'search_count': count
    }
    return HttpResponse(template.render(context, request))

# customerdetails_list() retrieves all customer details from the database and stores them in a QuerySet. The
# customerdetails.html page is loaded with the QuerySet loaded as a variable in context
def customerdetails_list(request):
    customerList = CustomerDetails.objects.all

    template = loader.get_template('WebApp/customerdetails.html')
    context = {
        'customer_list': customerList
    }
    return HttpResponse(template.render(context, request))

# Stores the Store ID of the clicked Store Link in Stores.html for future use
def storeDetails(request):
    storeid = request.GET.get('id')
    store = StoreDetail.objects.get(storeID=storeid)
    template = loader.get_template('WebApp/individualStore.html')
    context = {
        'storeObj': store
    }
    return HttpResponse(template.render(context, request))

# Filters the Rental History database using the StoreID as a filter.
def rentalHistory(request):
    storeid = request.GET.get('id')
    rentalList = RentalHistory.objects.filter(
        Q(storeID=storeid)
    )
    template = loader.get_template('WebApp/rentalHistory.html')
    context = {
        'rental_list': rentalList
    }
    return HttpResponse(template.render(context, request))