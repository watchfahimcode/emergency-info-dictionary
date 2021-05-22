from django.shortcuts import render
from django.http import HttpResponse
from .models import Union_council


# Create your views here.
def showUnionCouncilInfo(inputDistrict="",inputSubdistrict=""):
    return Union_council.objects.filter(district=inputDistrict,subdistrict=inputSubdistrict)