from django.shortcuts import render

from notes.models import Note


def index(request):
    """ A view to return the index page"""

    notes = Note.objects.all()
    urgent = notes.filter(urgent = True)

    context = {
        'notes': notes,
        'urgent': urgent,
    }

    return render(request, 'home/index.html', context)
