from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    slideries = Slider.objects.all()
    events = Event.objects.all()

    context = {
       'slideries': slideries,
       'events': events 
    }
    return render(request, 'web/index.html', context=context)

def single_event(request,id):
    events = Event.objects.get(id=id)
    tips = Tip.objects.filter(event=events)
    context = {
        'tips': tips,
        'events': events
    }
    
    return render(request, 'web/single-event.html', context=context)

def booking(request):
    return render(request, 'web/booking.html')
    
