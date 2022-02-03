from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Note, Category


@login_required
def notes(request):
    """ A view to return the notes page """

    notes = Note.objects.all()
    query = None
    categories = None
    urgentcheck = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            notes = notes.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'urgent' in request.GET:
            urgentcheck = request.GET['urgent'].split(',')
            notes = notes.filter(urgent = True)
            urgentcheck = Note.objects.filter(urgent = True)

    context = {
        'notes': notes,
        'search_term': query,
    }

    return render(request, 'notes/notes.html', context)


@login_required
def delete_note(request, note_id):
    """ Delete a note from the notes page """

    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect(reverse('notes'))
