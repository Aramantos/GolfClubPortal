from django.contrib import admin
from .models import Housing, HousingType

# Register your models here.


class HousingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
    )

    ordering = ('title',)


class HousingTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Housing, HousingAdmin)
admin.site.register(HousingType, HousingTypeAdmin)