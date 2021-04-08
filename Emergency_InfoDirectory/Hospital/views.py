from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital


# Create your views here.
def showHospitalInfo(inputDistrict=""):
    if inputDistrict=="":
        return Hospital.objects.all()
    return Hospital.objects.filter(district=inputDistrict)