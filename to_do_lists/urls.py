from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_do_lists, name='to_do_lists'),
    path('delete/<int:list_id>/', views.delete_list, name='delete_list'),
    path('add_list/', views.add_list, name='add_list'),
    path('add_list_item/', views.add_list_item, name='add_list_item'),
    path('done/<int:list_item_id>/', views.done_list_item, name='done_list_item'),
    path('undone/<int:list_item_id>/', views.undone_list_item, name='undone_list_item'),
]
