from django import forms
from django.forms import ModelForm
from .models import BookAppointment
import datetime


class DateInput(forms.DateInput):
    """
   calendar showing when choosing the date.
credits: https://webpedia.net/how-to-use-datepicker-in-django
     """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'text'


class BookingForm(forms.ModelForm):
    """
    Presents the booking form to the user.
    Dates to choose from is at
    least one day in future, and a maximum
    of 25 days.
    """
    class Meta:
        model = BookAppointment
        fields = ('first_name',
                  'last_name',
                  'email',
                  'date_for_visit',
                  'time_for_visit',)
        widgets = {
            'date_for_visit': DateInput(attrs={
                'min': datetime.date.today()+datetime.timedelta(days=1),
                'max': datetime.date.today()+datetime.timedelta(days=25)}),
            'time_for_visit': TimeInput(attrs={
                'class': 'timepicker'}),
        }


class EditBooking(forms.ModelForm):
    """
    Without the restrictions of at least
    one day in the future. Because a
    staff member should be able to update
    the booking if needed.
    """
    class Meta:
        model = BookAppointment
        fields = ('first_name',
                  'last_name',
                  'email',
                  'date_for_visit',
                  'time_for_visit',)
        widgets = {
            'date_for_visit': DateInput(attrs={
                'min': datetime.date.today(),
                'max': datetime.date.today()+datetime.timedelta(days=25)}),
            'time_for_visit': TimeInput()
        }
