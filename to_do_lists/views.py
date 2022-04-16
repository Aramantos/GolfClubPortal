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
    list_items = ListItem.objects.all()

    formList = ListForm
    formListItem = ListItemForm

    # if request.method == 'POST':
    #     if request.POST.get("form_type") == 'formOne':
    #         form = formList(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect(reverse('to_do_lists'))
    #     elif request.POST.get("form_type") == 'formTwo':
    #         form = formListItem(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect(reverse('to_do_lists'))

    context = {
        'lists': lists,
        'list_items': list_items,
        'formList': formList,
        'formListItem': formListItem,
    }

    return render(request, 'to_do_lists/to_do_lists.html', context)


@login_required
def add_list(request):
    """ Add a list to the to do lists page """

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Successfully added your booking')
            return redirect(reverse('to_do_lists'))
        else:
            print("error")
            # messages.error(request, 'Failed to add your booking. Please ensure the form is valid.')
    else:
        form = ListForm()

    context = {
        'form': form,
    }

    return render(request, context)


@login_required
def delete_list(request, list_id):
    """ Delete a list from the lists page """

    list = get_object_or_404(List, pk=list_id)
    list.delete()
    return redirect(reverse('to_do_lists'))


@login_required
def add_list_item(request):
    """ Add a list item to a list on the to do lists page """

    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Successfully added your booking')
            return redirect(reverse('view_bookings'))
        else:
            print("error")
            # messages.error(request, 'Failed to add your booking. Please ensure the form is valid.')
    else:
        form = ListItemForm()

    context = {
        'form': form,
    }

    return render(request, context)


@login_required
def done_list_item(request, list_item_id):
    """ Set a list item to done the list_items page """

    list_item = get_object_or_404(ListItem, pk=list_item_id)
    list_item.done = False
    list_item.save()

    return redirect(reverse('to_do_lists'))


@login_required
def undone_list_item(request, list_item_id):
    """ Set a list item to undone on the list_items page """

    list_item = get_object_or_404(ListItem, pk=list_item_id)
    list_item.done = True
    list_item.save()

    return redirect(reverse('to_do_lists'))
