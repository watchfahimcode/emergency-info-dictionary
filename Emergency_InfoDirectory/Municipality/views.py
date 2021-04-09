from django.shortcuts import render
from .models import Municipality

# Create your views here.
def showMunicipalityInfo(inputDistrict=""):
    if inputDistrict=="":
        return Municipality.objects.all()
    return Municipality.objects.filter(district=inputDistrict)