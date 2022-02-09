from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Housing, HousingType


@login_required
def housing_list(request):
    """ A view to return the housing list page """

    housing = Housing.objects.all()

    context = {
        'housing': housing,
    }

    return render(request, 'bookings/housing.html', context)


@login_required
def water_check(request, housing_id):
    """ Change status of the water """

    housing = get_object_or_404(Housing(), pk=housing_id)
    if housing.water:
        housing.water = False
        housing.save()

    else:
        housing.water = True
        housing.save()

    return redirect(reverse('housing'))


@login_required
def heat_check(request, housing_id):
    """ Change status of the water """

    housing = get_object_or_404(Housing(), pk=housing_id)
    if housing.heat:
        housing.heat = False
        housing.save()

    else:
        housing.heat = True
        housing.save()

    return redirect(reverse('housing'))


@login_required
def clean_check(request, housing_id):
    """ Change status of the water """

    housing = get_object_or_404(Housing(), pk=housing_id)
    if housing.clean:
        housing.clean = False
        housing.save()

    else:
        housing.clean = True
        housing.save()

    return redirect(reverse('housing'))