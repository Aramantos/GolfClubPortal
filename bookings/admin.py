from django.contrib import admin
from .models import Housing, HousingType, Booking

# Register your models here.


class HousingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
        'water',
        'heat',
        'clean',
    )

    ordering = ('title',)


class HousingTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'housing',
        'checkin_date',
        'checkout_date',
    )



admin.site.register(Housing, HousingAdmin)
admin.site.register(HousingType, HousingTypeAdmin)
admin.site.register(Booking, BookingAdmin)
