from django.shortcuts import render
from .settings import *
import table.models
import pyodbc


def home(request):
	return render(request, 'table/home.html')


def CustomerView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Customer WHERE CustomerID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/customer.html', {'CustomerModel':result, 'title':'Customer', 'table_name':'Customer'})


def DateView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Date WHERE TheYear=2009')
	result = cursor.fetchall()
	return render(request, 'table/date.html', {'DateModel':result, 'title':'Date', 'table_name':'Date'})


def OrderView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.FactOrder WHERE ID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/order.html', {'OrderModel':result, 'title':'Order', 'table_name':'Order'})


def LocationView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Location WHERE LocationID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/location.html', {'LocationModel':result, 'title':'Location', 'table_name':'Location'})


def ProductView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Product WHERE ID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/product.html', {'ProductModel':result, 'title':'Product', 'table_name':'Product'})
