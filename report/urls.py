from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reports-home'),
    path('country/', views.CountryChartView.as_view(), name='reports-country'),
    #path('date/', views.DateView, name='tables-date'),
    #path('order/', views.OrderView, name='tables-order'),
    #path('location/', views.LocationView, name='tables-location'),
    #path('product/', views.ProductView, name='tables-product'),
]
