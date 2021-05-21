from django.shortcuts import render
from django.http import HttpResponse
from .models import Police_station


# Create your views here.
def showPoliceStationInfo(inputDistrict,inputSubdistrict=""):
    return Police_station.objects.filter(district=inputDistrict,subdistrict=inputSubdistrict)