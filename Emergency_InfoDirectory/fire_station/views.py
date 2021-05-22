from django.shortcuts import render
from django.http import HttpResponse
from .models import FireStation


# Create your views here.
def showFireStationInfo(inputDistrcit="",inputSubdistrict=""):
    return FireStation.objects.filter(district=inputDistrcit,subdistrict=inputSubdistrict)