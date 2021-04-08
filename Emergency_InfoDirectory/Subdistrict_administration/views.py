from django.shortcuts import render
from .models import Subdistrict_administration

# Create your views here.
def showSubdistrictAdminInfo(inputDistrict=""):
    if inputDistrict=="":
        return Subdistrict_administration.objects.all()
    return Subdistrict_administration.objects.filter(district=inputDistrict)