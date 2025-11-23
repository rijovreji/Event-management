from Eventapp.models import Event
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def event(request):

    dict_eve ={
        'eve' : Event.objects.all()
    }
    return render(request,'events.html',dict_eve)
def booking(request):
    return render(request,'booking.html')
def contact(request):
    return render(request,'contact.html')