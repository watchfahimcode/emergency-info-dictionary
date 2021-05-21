from django.shortcuts import render
from .models import Bazar
# Create your views here.
def showBazarInfo(inputDistrict="",inputSubdistrict="",):
    return Bazar.objects.filter(district=inputDistrict,subdistrict=inputSubdistrict)