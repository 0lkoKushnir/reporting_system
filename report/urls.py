from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reports-home'),
    path('country/', views.CountryChartView.as_view(), name='reports-country'),
    path('sales-region-category/', views.SalesRegionCategoryChartView.as_view(), name='reports-sales-region-category'),
    path('sales-usa-category/', views.SalesUSACategoryChartView.as_view(), name='reports-sales-usa-category'),
    path('sales-nonusa-category/', views.SalesNONUSACategoryChartView.as_view(), name='reports-sales-nonusa-category'),
    path('sales-country-month/', views.SalesCountryMonthChartView.as_view(), name='reports-sales-country-month'),
    #path('order/', views.OrderView, name='tables-order'),
    #path('location/', views.LocationView, name='tables-location'),
    #path('product/', views.ProductView, name='tables-product'),
]
