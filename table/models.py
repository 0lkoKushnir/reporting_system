from django.db import models

class CustomerModel(models.Model):
	ID = models.IntegerField()
	FullName = models.CharField(max_length=101)
	Age = models.IntegerField()
	Income = models.IntegerField()
	Gender = models.CharField(max_length=10)


class DateModel(models.Model):
	ID = models.IntegerField()
	Date = models.DateField()
	Day = models.IntegerField()
	Month = models.CharField(max_length=50)
	Year = models.IntegerField()
	Weekday = models.CharField(max_length=50)
	WeekInYear = models.IntegerField()
	WeekInMonth = models.IntegerField()


class OrderModel(models.Model):
	ID = models.IntegerField()
	Order = models.IntegerField()
	Location = models.IntegerField()
	Product = models.IntegerField()
	Customer = models.IntegerField()
	Date = models.IntegerField
	Quantity = models.IntegerField()
	NetAmount = models.FloatField()
	Tax = models.FloatField()
	TotalAmount = models.FloatField()


class LocationModel(models.Model):
	ID = models.IntegerField()
	Region = models.CharField(max_length=50)
	Country = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	City = models.CharField(max_length=50)


class ProductModel(models.Model):
	ID = models.IntegerField()
	Title = models.CharField(max_length=50)
	Actor = models.CharField(max_length=50)
	Category = models.CharField(max_length=50)
	Price = models.FloatField()
	Special = models.CharField(max_length=5)