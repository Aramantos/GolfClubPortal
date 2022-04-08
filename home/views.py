from django.shortcuts import render

from notes.models import Note
from bookings.models import Booking

from datetime import date, timedelta


def index(request):
    """ A view to return the index page"""

    notes = Note.objects.all()
    bookings = Booking.objects.all()

    urgent = notes.filter(urgent=True)

    tday = date.today()
    tmrw = tday + timedelta(days=1)
    next_seven_days = date.today() + timedelta(days=7)
    next_month = date.today() + timedelta(days=30)
    tday_bookings = bookings.filter(checkin_date=tday)
    tmrw_bookings = bookings.filter(checkin_date=tmrw)
    bookings_month = bookings.filter(checkin_date__gte=tday, checkin_date__lte=next_month)
    bookings_week = bookings.filter(checkin_date__gte=tday, checkin_date__lte=next_seven_days)

    context = {
        'notes': notes,
        'urgent': urgent,
        'bookings': bookings,
        'tday_bookings': tday_bookings,
        'tmrw_bookings': tmrw_bookings,
        'next_seven_days': next_seven_days,
        'next_month': next_month,
        'bookings_month': bookings_month,
        'bookings_week': bookings_week,
    }

    return render(request, 'home/index.html', context)
