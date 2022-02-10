from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.housing_list, name='housing_list'),
    path('water_check/<int:housing_id>/', views.water_check, name='water_check'),
    path('heat_check/<int:housing_id>/', views.heat_check, name='heat_check'),
    path('clean_check/<int:housing_id>/', views.clean_check, name='clean_check'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('add_booking/<int:booking_id>/', views.add_booking, name='add_booking'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]
