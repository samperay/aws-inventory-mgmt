from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'inventory-home' ),
    path('getdata/', views.getdata, name = 'inventory-getdata'),
]
