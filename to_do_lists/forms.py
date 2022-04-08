from django import forms
from .models import List, ListItem


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = '__all__'


class ListItemForm(forms.ModelForm):

    class Meta:
        model = List
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lists = List.objects.all()
