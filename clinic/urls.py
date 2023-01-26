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
    path('booking.html', views.booking, name='booking')

]
