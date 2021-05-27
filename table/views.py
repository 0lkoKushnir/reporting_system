from django.shortcuts import render
import table.models
from django.http import HttpResponse
import pyodbc
from .settings import *


def home(request):
	return HttpResponse('<h1>HOME TABLES</h1>')


def CustomerView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Customer WHERE CustomerID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/customer.html', {'CustomerModel' : result})


def DateView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Date WHERE TheYear=2009')
	result = cursor.fetchall()
	return render(request, 'table/date.html', {'DateModel' : result})


def OrderView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.FactOrder WHERE ID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/order.html', {'OrderModel' : result})


def LocationView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Location WHERE LocationID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/location.html', {'LocationModel' : result})


def ProductView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Product WHERE ID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/product.html', {'ProductModel' : result})
