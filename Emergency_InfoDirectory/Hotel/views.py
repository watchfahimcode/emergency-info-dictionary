from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel


# Create your views here.
def showHotelInfo(inputDistrict="",inputSubdistrict=""):
    return Hotel.objects.filter(district=inputDistrict,subdistrict=inputSubdistrict)