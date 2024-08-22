from django.urls import path
from . import views

urlpatterns = [
    path('cars', views.getData),
    path('add/', views.addCar)
]