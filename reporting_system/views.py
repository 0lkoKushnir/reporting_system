
from django.shortcuts import render
from .settings import *
import pyodbc


def home(request):
	return render(request, 'rs/home.html')
'''
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>HOME</h1>')'''