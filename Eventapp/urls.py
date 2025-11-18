from django.urls import path
from Eventapp import views

urlpatterns = [
    path('', views.index, name="index"),  # blank space is used for fist see the page thats why
    path('about/', views.about, name='about'),
    path('event/', views.event, name='event'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),

]
