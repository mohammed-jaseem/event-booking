from django import forms
from web.models import *
from users.models import User

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['image', 'title']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['image', 'name']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['image', 'name', 'phone', 'short_description','place',]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'short_discription': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'short_discription'}),  
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'Participant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Participant'}),
        }


class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['image', 'name', 'title', 'short_description','event',]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_discription': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'short_discription'}),  
            'event': forms.Select(attrs={'class': 'form-control'}),
        }