from django.shortcuts import render
from .models import Subdistrict_administration

# Create your views here.
def showSubdistrictAdminInfo(inputDistrict="",inputSubdistrict=""):
    return Subdistrict_administration.objects.filter(district=inputDistrict,subdistrict=inputSubdistrict)