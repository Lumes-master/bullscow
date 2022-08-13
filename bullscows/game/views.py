from django.http import HttpResponse
from django.shortcuts import render
from .models import Bullscows



# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def bullscows(request):
    pass