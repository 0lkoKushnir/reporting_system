from django.contrib import admin
from .models import CountryModel, SalesRegionCategoryModel, SalesCountryMonthModel

admin.site.register(CountryModel)
admin.site.register(SalesRegionCategoryModel)
admin.site.register(SalesCountryMonthModel)