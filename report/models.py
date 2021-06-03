from django.db import models


class CountryModel(models.Model):
	Country = models.CharField(max_length=50)
	NetAmount = models.IntegerField()
	Tax = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.Country)


class SalesRegionCategoryModel(models.Model):
	Region = models.CharField(max_length=50)
	Category = models.CharField(max_length=50)
	Quantity = models.IntegerField()
	Orders = models.IntegerField()
	Income = models.IntegerField()

	def __str__(self):
		return '{} - {}'.format(self.Region, self.Category)


class SalesCountryMonthModel(models.Model):
	Country = models.CharField(max_length=50)
	Month = models.CharField(max_length=50)
	NetAmount = models.IntegerField(default=10000)
	Tax = models.IntegerField(default=1000)
	TotalAmount = models.IntegerField()

	def __str__(self):
		return '{} - {}'.format(self.Country, self.Month)