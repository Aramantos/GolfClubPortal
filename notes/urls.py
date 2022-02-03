from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]