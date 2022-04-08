from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_do_lists, name='to_do_lists'),
    # path('add/', views.add_note, name='add_note'),
    # path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    # path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
