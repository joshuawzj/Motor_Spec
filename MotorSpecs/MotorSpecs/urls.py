"""MotorSpecs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import WebApp.views
import DataRepresent.views
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WebApp.views.home, name='home'),
    path('home/', WebApp.views.home, name='home'),
    path('login/', LoginView.as_view(template_name='WebApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('dashboard/', WebApp.views.dashboard, name='dashboard'),
    path('aboutus/', WebApp.views.aboutUs, name='aboutUs'),
    path('stores/', WebApp.views.Stores, name='Stores'),
    path('legalresources/', WebApp.views.LegalResources, name='LegalResources'),
    path('faqs/', WebApp.views.faqs, name='faqs'),
    path('contact/', WebApp.views.contact, name='contact'),
    url(r'^dashboard/results/$', WebApp.views.search_list, name='search'),
    url(r'^home/results/$', WebApp.views.CustomerSearch_list, name='customerSearch'),
    path('vehiclelist/', include('VehicleList.urls')),
    path('rentaltrends/', DataRepresent.views.rentaltrends, name='rentaltrends'),
    path('storetrends/', DataRepresent.views.storetrends, name='storetrends'),
    path('vehiclerecommendation/', WebApp.views.vehicleRecommendation, name='vehiclerecommendation'),
    path('customerdetails/', WebApp.views.customerdetails_list, name='customerdetails'),
    path('vehiclerecommendationresults/', WebApp.views.vehicleRecommendationResult, name='vehiclerecommendationresults'),
    url(r'^stores/?id=[0-9]+/', WebApp.views.storeDetails, name='storedetails'),
    url(r'^stores/storesid=[0-9]+/rentalhistory/', WebApp.views.rentalHistory, name='rentalhistory'),
    path('register/',WebApp.views.register,name='register'),
]
