from django.shortcuts import render

from notes.models import Note
from bookings.models import Booking

from datetime import date


def index(request):
    """ A view to return the index page"""

    notes = Note.objects.all()
    bookings = Booking.objects.all()

    urgent = notes.filter(urgent = True)

    tday = date.today()
    tday_bookings = bookings.filter(checkin_date = tday)

    context = {
        'notes': notes,
        'urgent': urgent,

        'bookings': bookings,
        'tday_bookings': tday_bookings,
    }

    return render(request, 'home/index.html', context)
