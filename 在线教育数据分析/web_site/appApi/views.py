from django.shortcuts import render,HttpResponse
from appApi.interface.interface import daily_interface, weekly_interface

# Create your views here.

def daily_handler(request):
    return HttpResponse(daily_interface())

def weekly_handler(request):
    return HttpResponse(weekly_interface())