from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tables-home'),
    path('customer/', views.CustomerView, name='tables-customer'),
    path('customer/agregated', views.CustomerAgrView, name='tables-customer-agr'),
    path('date/', views.DateView, name='tables-date'),
    path('order/', views.OrderView, name='tables-order'),
    path('location/', views.LocationView, name='tables-location'),
    path('location/agregated', views.LocationAgrView, name='tables-location-agr'),
    path('product/', views.ProductView, name='tables-product'),
]
