from django.shortcuts import render

from .models import Note


def notes(request):
    """ A view to return the shop page """

    notes = Note.objects.all()

    context = {
        'notes': notes,
    }

    return render(request, 'notes/notes.html', context)