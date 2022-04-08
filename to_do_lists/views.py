from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import List, ListItem
from .forms import ListForm, ListItemForm

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


@login_required
def to_do_lists(request):
    """ A view to return the notes page """

    lists = List.objects.all()
    # categories = None
    # urgentcheck = None

    # if request.GET:
    #     if 'category' in request.GET:
    #         categories = request.GET['category'].split(',')
    #         notes = notes.filter(category__name__in=categories)
    #         categories = Category.objects.filter(name__in=categories)

    #     if 'urgent' in request.GET:
    #         urgentcheck = request.GET['urgent'].split(',')
    #         notes = notes.filter(urgent = True)
    #         urgentcheck = Note.objects.filter(urgent = True)

    context = {
        'lists': lists,
    }

    return render(request, 'notes/notes.html', context)


@login_required
def add_list(request):
    """ Add an note to the notes page """

    user = request.user.username
    print(user)

    if request.method == 'POST':
        form = ListForm(request.POST)
        ListForm(initial={'created_by': user})
        if form.is_valid():
            form.save()
            print("success")
            # messages.success(request, 'Successfully added your image')
            return redirect(reverse('to_do_lists'))
        else:
            print("error")
            # messages.error(request, 'Failed to add your image. Please ensure the form is valid.')
    else:
        form = ListForm()

    template = 'to_do_lists/add_list.html'
    context = {
        'form': form,
        'user': user,
    }

    return render(request, template, context)


# @login_required
# def edit_list(request, note_id):
#     """ Edit an note on the notes page """

#     note = get_object_or_404(List, pk=list_id)
#     note.urgent = False
#     note.save()

#     return redirect(reverse('notes'))


# @login_required
# def delete_note(request, note_id):
#     """ Delete a note from the notes page """

#     note = get_object_or_404(List, pk=note_id)
#     note.delete()
#     return redirect(reverse('notes'))
