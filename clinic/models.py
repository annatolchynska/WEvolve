from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class BookAppointment(models.Model):
    """
    Model for storing the bookings to the database
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
        )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    date_for_visit = models.DateField(null=True)
    time_for_visit = models.TimeField(default=datetime.time(10, 00))

    def save(self, *args, **kwargs):
        if self.date_for_visit < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(BookAppointment, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.first_name
