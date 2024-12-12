from django.shortcuts import render, reverse
from web.models import *
from django.http import HttpResponseRedirect
from manager.forms import *
from main.functions import generate_form_errors


def index(request):
    
    return render(request,'manager/index.html')

def slideries(request):
    instances = Slider.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/slideries.html', context=context)

def delete_slideries(request,id):
    instance = Slider.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:slideries'))

def slideries_add(request,):
    if request.method == 'POST':   
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:slideries'))
            
        else:
            message = generate_form_errors(form)
            form = SliderForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/slideries_add.html', context=context)



    else:
        form = SliderForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/slideries_add.html', context=context)

def edit_slideries(request, id):
    instance = Slider.objects.get(id=id)
    if request.method == 'POST':   
        form = SliderForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:slideries'))
            
        else:
            message = generate_form_errors(form)
            form = SliderForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/slideries_add.html', context=context)



    else:
        form = SliderForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/slideries_add.html', context=context)



def events(request):
    instances = Event.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/events.html', context=context)

def delete_events(request,id):
    instance = Event.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:events'))

def events_add(request,):
    if request.method == 'POST':   
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:events'))
            
        else:
            message = generate_form_errors(form)
            form = EventForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/events_add.html', context=context)



    else:
        form = EventForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/events_add.html', context=context)

def edit_events(request, id):
    instance = Event.objects.get(id=id)
    if request.method == 'POST':   
        form = EventForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:events'))
            
        else:
            message = generate_form_errors(form)
            form = EventForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/events_add.html', context=context)



    else:
        form = EventForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/events_add.html', context=context)



def form(request):
    instances = Form.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/forms.html', context=context)

def delete_forms(request,id):
    instance = Form.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:forms'))

def forms_add(request,):
    if request.method == 'POST':   
        form = FormForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:forms'))
            
        else:
            message = generate_form_errors(form)
            form = FormForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/forms_add.html', context=context)



    else:
        form = FormForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/forms_add.html', context=context)

def edit_forms(request, id):
    instance = Form.objects.get(id=id)
    if request.method == 'POST':   
        form = FormForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:forms'))
            
        else:
            message = generate_form_errors(form)
            form = FormForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/forms_add.html', context=context)



    else:
        form = FormForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/forms_add.html', context=context)


def tips(request):
    instances = Tip.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/tips.html', context=context)

def delete_tips(request,id):
    instance = Tip.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:tips'))

def tips_add(request,):
    if request.method == 'POST':   
        form = TipForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:tips'))
            
        else:
            message = generate_form_errors(form)
            form = TipForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/tips_add.html', context=context)



    else:
        form = TipForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/tips_add.html', context=context)

def edit_tips(request, id):
    instance = Tip.objects.get(id=id)
    if request.method == 'POST':   
        form = TipForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:tips'))
            
        else:
            message = generate_form_errors(form)
            form = TipForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/tips_add.html', context=context)



    else:
        form = TipForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/tips_add.html', context=context)




