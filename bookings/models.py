from django.db import models


class HousingType(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Housing(models.Model):

    type = models.ForeignKey('HousingType', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    description = models.TextField()
    water = models.BooleanField(default=False)
    heat = models.BooleanField(default=False)
    clean = models.BooleanField(default=False)

    def __str__(self):
        return self.title