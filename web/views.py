from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/login')
def index(request):
    slideries = Slider.objects.all()
    events = Event.objects.all()
    projects = Project.objects.all()

    context = {
       'slideries': slideries,
       'events': events,
       'projects': projects
    }
    return render(request, 'web/index.html', context=context)

@login_required(login_url='/login')
def single_event(request,id):
    events = Event.objects.get(id=id)
    tips = Tip.objects.filter(event=events)
    projects = Project.objects.all()
    forms = Form.objects.filter(name=events)

    context = {
        'tips': tips,
        'events': events,
        'projects': projects,
        'forms': forms,

    }
    
    return render(request, 'web/single-event.html', context=context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 

        user = authenticate(request, email=email, password=password,) 

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            context = {
                'error':True,
                'message':'Invalid email or password'
            }
            return render(request, 'web/login.html', context=context)
    else:
        return render(request, 'web/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            email=email,
            password=password,
            is_customer=True
        )
        user.save()
        customer = Customer.objects.create(
            user=user
        )
        customer.save()
        return HttpResponseRedirect(reverse('web:login'))
    else:
        return render(request, 'web/register.html')
    
def logout(request):
    user = request.user
    auth_logout(request)

    return HttpResponseRedirect(reverse('web:login'))

def add_event(request):
    return render(request, 'web/add-event.html')

def form(request):
    user =request.user
    customer = Customer.objects.get(user=user)
    events = Event.objects.all()

    if request.method == 'POST':
        event_id = request.POST.get('event_type')
        name = Event.objects.get(id=event_id)
        short_description = request.POST.get('short_description')
        place = request.POST.get('place')
        Participant = request.POST.get('Participant')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')

        form = Form.objects.create(
            name=name, 
            short_description=short_description,
            place=place,
            Participant=Participant,
            phone=phone,    
            image=image,
        )
        
        form.save()

    context = {
        'customer': customer,
        'events': events,
    }
    return render(request, 'web/form.html', context=context)


    
