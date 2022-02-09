from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.housing_list, name='housing_list'),
    path('water_check/<int:housing_id>/', views.water_check, name='water_check'),
    path('heat_check/<int:housing_id>/', views.heat_check, name='heat_check'),
    path('clean_check/<int:housing_id>/', views.clean_check, name='clean_check'),
]
