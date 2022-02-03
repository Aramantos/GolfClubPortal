from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Note


@login_required
def notes(request):
    """ A view to return the shop page """

    notes = Note.objects.all()

    context = {
        'notes': notes,
    }

    return render(request, 'notes/notes.html', context)


@login_required
def delete_note(request, note_id):
    """ Delete a note from the notes page """

    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect(reverse('notes'))
