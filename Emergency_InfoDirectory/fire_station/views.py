from django.shortcuts import render
from django.http import HttpResponse
from .models import FireStation


# Create your views here.
def showFireStationInfo(inputDistrcit=""):
    if inputDistrcit=="":
        return FireStation.objects.all()
    return FireStation.objects.filter(district=inputDistrcit)