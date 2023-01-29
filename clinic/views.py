from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BookAppointment
from .forms import BookingForm, EditBooking


def home(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def mental(request):
    return render(request, 'mental.html', {})


def holistic(request):
    return render(request, 'holistic.html', {})


def addiction(request):
    return render(request, 'addiction.html', {})


def costs(request):
    return render(request, 'costs.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def error404(request, exception):
    return render(request, 'error404.html')


@login_required
def booking(request):
    """
    Views the booking form and checks that the
    input is valid before submitting. If it is
    not, a message will show and redirect back
    to the form.
    """
    if request.method == 'POST':
        booking = BookAppointment(user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking placed successfully.')
            return redirect('booking')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})


@login_required
def view_booking(request):
    """
    Lets staff member view all bookings, and
    regular user only his own bookings.
    """
    if request.user.is_staff:
        bookings = BookAppointment.objects.all()
    else:
        bookings = request.user.bookings.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'useraccount.html', context)


@login_required
def delete_booking(request, booking_id):
    """
    Deletes booking
    """
    if request.user.is_staff:
        try:
            booking = get_object_or_404(BookAppointment, id=booking_id)
            booking.delete()
            messages.success(request, 'Booking deleted successfully.')
            return redirect('useraccount')
        except Http404 as err:
            messages.error(request, 'Oops, booking not found.')
            return redirect('useraccount')
    else:
        return redirect('home')


@login_required
def edit_booking(request, booking_id):
    """
    Presents the booking form with the recent informtion added.
    When update is done update
    has been made.
    """
    try:
        booking = get_object_or_404(BookAppointment, id=booking_id)
        if request.method == 'POST':
            form = EditBooking(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                messages.success(request, 'Updated successfully!')
                return redirect('useraccount')
        else:
            form = EditBooking(instance=booking)
        context = {
                'form': form
            }
        return render(request, 'edit_booking.html', context)
    except Http404 as err:
        messages.error(request, 'Sorry, booking not found.')
        return redirect('useraccount')


@login_required
def view_users(request):
    """
    Let staff memebers view all the users.
    """
    if request.user.is_staff:
        users = User.objects.all()
        context = {
            'users': users,
        }
        return render(request, 'users.html', context)
    else:
        return redirect('home')


@login_required
def delete_user(request, user_id):
    """
    Let staff member delete a user.
    If the user does not exist, a message
    will show.
    """
    if request.user.is_staff:
        try:
            user = get_object_or_404(User, id=user_id)
            user.delete()
            messages.success(request, 'User deleted successfully.')
            return redirect('users')
        except Http404 as err:
            messages.error(request, 'Oops, user not found.')
            return redirect('users')
    else:
        messages.error(request, 'You do not have permission to do this.')
        return redirect('home')
