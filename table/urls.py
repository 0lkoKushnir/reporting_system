from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tables-home'),
    path('customer/', views.CustomerView),
    path('date/', views.DateView),
    path('order/', views.OrderView),
    path('location/', views.LocationView),
    path('product/', views.ProductView),
]
