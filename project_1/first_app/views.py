from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("This is course page")
def about(request):
    return HttpResponse("This is about page")
def home(request):
    return HttpResponse("This is home page under first app")
