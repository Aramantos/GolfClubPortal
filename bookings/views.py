from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Housing, HousingType, Booking

from .forms import BookingForm

from datetime import date, datetime, timedelta


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

    h_types = None

    this_day = date.today()
    next_day = this_day + timedelta(days=1)
    seven_days = date.today() + timedelta(days=7)
    next_month = date.today() + timedelta(days=30)
    last_month = date.today() + timedelta(days=-30)
    past_bookings = bookings.filter(checkout_date__lte=this_day)

    if request.GET:
        if 'housing_type' in request.GET:
            h_types = request.GET['housing_type'].split(',')
            bookings = Booking.objects.filter(housing__h_type__name__in=h_types)
            # h_types = HousingType.objects.filter(name__in=h_types)

        if 'this_day' in request.GET:
            bookings = bookings.filter(checkin_date=this_day)
        if 'next_day' in request.GET:
            bookings = bookings.filter(checkin_date=next_day)
        if 'next_seven_days' in request.GET:
            bookings = bookings.filter(checkin_date__gte=this_day, checkin_date__lte=seven_days)
        if 'next_month' in request.GET:
            bookings = bookings.filter(checkin_date__gte=this_day, checkin_date__lte=next_month)
        if 'past_bookings' in request.GET:
            bookings = bookings.filter(checkout_date__lte=this_day)
        if 'last_month' in request.GET:
            bookings = bookings.filter(checkout_date__gte=last_month, checkout_date__lte=this_day)

    context = {
        'bookings': bookings,
        'this_day': this_day,
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
            # messages.success(request, 'Successfully added your booking')
            print("success")
            return redirect(reverse('view_bookings'))
        else:
            print("error")
            # messages.error(request, 'Failed to add your booking. Please ensure the form is valid.')
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
            # messages.success(request, 'Successfully updated the booking!')
            print("success")
            return redirect(reverse('gallery'))
        else:
            print("error")
            # messages.error(request, 'Failed to update booking. Please ensure the form is valid.')
    else:
        form = BookingForm(instance=booking)
        # messages.info(request, f'You are editing the booking for order number {image.order_number}')

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
