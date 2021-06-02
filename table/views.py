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
	return render(request, 'table/customer.html', {'CustomerModel':result, 'title':'Клієнти', 'table_name':'Клієнти'})


def CustomerAgrView(request):
	return render(request, 'table/customerAgr.html', {'title':'Дані про таблицю "Клієнти"', 'table_name':'Дані про таблицю "Клієнти"'})


def DateView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Date WHERE TheYear=2009')
	result = cursor.fetchall()
	return render(request, 'table/date.html', {'DateModel':result, 'title':'Дати', 'table_name':'Дати'})


def OrderView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.FactOrder WHERE ID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/order.html', {'OrderModel':result, 'title':'Замовлення', 'table_name':'Замовлення'})


def LocationView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Location WHERE LocationID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/location.html', {'LocationModel':result, 'title':'Локації', 'table_name':'Локації'})


def LocationAgrView(request):
	return render(request, 'table/locationAgr.html', {'title':'Дані про таблицю "Локації"', 'table_name':'Дані про таблицю "Локації"'})


def ProductView(request):
	conn = pyodbc.connect('Driver=%s;Server=%s;Database=%s;Trusted_Connection=yes;'%(driver, server, database))
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM dbo.Product WHERE ID <= 1000')
	result = cursor.fetchall()
	return render(request, 'table/product.html', {'ProductModel':result, 'title':'Товари', 'table_name':'Товари'})
