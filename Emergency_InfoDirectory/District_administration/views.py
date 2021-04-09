from django.shortcuts import render
from .models import District_administration

# Create your views here.
def showDistrictAdminInfo(inputDistrict=""):
    if inputDistrict=="":
        return District_administration.objects.all()
    return District_administration.objects.filter(district=inputDistrict)