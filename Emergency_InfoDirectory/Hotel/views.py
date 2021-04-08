from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel


# Create your views here.
def showHotelInfo(inputDistrict=""):
    if inputDistrict=="":
        return Hotel.objects.all()
    return Hotel.objects.filter(district=inputDistrict)