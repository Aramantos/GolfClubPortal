from django.contrib import admin
from .models import List, ListItem

# Register your models here.


class ListAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
        'created_by',
    )

    ordering = ('name',)


class ListItemAdmin(admin.ModelAdmin):
    list_display = (
        'list',
        'item',
        'created',
        'created_by',
    )


admin.site.register(List, ListAdmin)
admin.site.register(ListItem, ListItemAdmin)
