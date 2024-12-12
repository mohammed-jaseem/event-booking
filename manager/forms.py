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