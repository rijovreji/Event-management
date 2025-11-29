from Eventapp.models import Event
from django.shortcuts import render, redirect
from .forms import BookingForms
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

    if request.method=="POST":
        form=BookingForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=BookingForms()
    dict_form={
        'form':form
    }

    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')