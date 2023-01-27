from django.contrib import admin
from .models import BookAppointment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
# admin.site.register(PlaceBooking)


@admin.register(BookAppointment)
class BookAppointment(admin.ModelAdmin):
    """
    Displays the fields needed in admin page from BookAppointment model
    """
    list_display = (
        'first_name',
        'last_name',
        'email',
        'date_for_visit',
        'time_for_visit',
        'approved'
        )
    list_filter = ('approved', 'date_for_visit', 'created_on')
    search_fields = ('first_name', 'last_name', 'email')
