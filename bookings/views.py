from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Housing, HousingType, Booking

from .forms import BookingForm


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


@login_required
def view_bookings(request):
    """ A view to return the bookings page """

    bookings = Booking.objects.all()

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/bookings.html', context)


@login_required
def add_booking(request):
    """ Add an booking to the bookings page """

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            # messages.success(request, 'Successfully added your image')
            print("success")
            return redirect(reverse('bookings'))
        else:
            print("error")
            # messages.error(request, 'Failed to add your image. Please ensure the form is valid.')
    else:
        form = BookingForm()

    template = 'bookings/add_booking.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_booking(request, booking_id):
    """ Edit a booking in the bookings page """

    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Successfully updated the image!')
            print("success")
            return redirect(reverse('gallery'))
        else:
            print("error")
            # messages.error(request, 'Failed to update image. Please ensure the form is valid.')
    else:
        form = BookingForm(instance=booking)
        # messages.info(request, f'You are editing the image for order number {image.order_number}')

    template = 'bookings/edit_booking.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_booking(request, booking_id):
    """ Delete a booking from the bookings page """

    booking = get_object_or_404(Booking, pk=booking_id)
    booking.delete()
    return redirect(reverse('bookings'))
