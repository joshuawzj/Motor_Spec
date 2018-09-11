from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'loginapp/dashboard.html')
