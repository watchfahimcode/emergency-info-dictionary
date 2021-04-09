from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor


# Create your views here.
def showDoctorInfo(inputDistrict=""):
    if inputDistrict=="":
        return Doctor.objects.all()
    return Doctor.objects.filter(district=inputDistrict)