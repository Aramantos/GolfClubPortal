from django.contrib import admin
from .models import Note, Category

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created_by',
    )

    ordering = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)