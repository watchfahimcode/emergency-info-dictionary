from django.shortcuts import render
from .models import Bazar
# Create your views here.
def showBazarInfo(inputDistrict=""):
    if inputDistrict=="":
        return Bazar.objects.all()
    return Bazar.objects.filter(district=inputDistrict)