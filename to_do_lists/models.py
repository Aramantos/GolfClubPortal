from django.db import models
from django.contrib.auth.models import User


class List(models.Model):

    name = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ListItem(models.Model):
    
    list = models.ForeignKey('List', null=True, blank=True, on_delete=models.SET_NULL)
    item = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.item
