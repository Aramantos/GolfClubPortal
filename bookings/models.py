from django.db import models


class HousingType(models.Model):
    """ Type of housing available in the resort """

    class Meta:
        """ Change name in admin panel """
        verbose_name_plural = 'Housing Type'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ Get the user friendly name version of the model"""
        return self.friendly_name


class Housing(models.Model):
    """ Each of the specific housing types available """

    class Meta:
        """ Change name in admin panel """
        verbose_name_plural = 'Housing'

    h_type = models.ForeignKey('HousingType', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    description = models.TextField()
    water = models.BooleanField(default=False)
    heat = models.BooleanField(default=False)
    tidy = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """ Each of the bookings that are made at the resort """

    housing = models.ForeignKey('Housing', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    details = models.TextField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    def __str__(self):
        return self.name