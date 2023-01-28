from django.conf.urls import handler404, handler500
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name='about'),
    path('mental.html', views.mental, name='mental'),
    path('holistic.html', views.holistic, name='holistic'),
    path('addiction.html', views.addiction, name='addiction'),
    path('costs.html', views.costs, name='costs'),
    path('contact.html', views.contact, name='contact'),
    path('booking.html', views.booking, name='booking'),
    path('useraccount.html', views.view_booking, name='useraccount'),
    path('users.html', views.view_users, name='users'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
    path('edit/<booking_id>', views.edit_booking, name='edit'),
    path('delete_user/<user_id>', views.delete_user, name='delete_user'),

]
