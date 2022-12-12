from django import forms
from .models import HealthData
from django.forms import ModelForm

class HealthDataForm(ModelForm):
    class Meta:
        model = HealthData
        fields = (
            'weight', 'gl_level',
            # 'height', 
            'day'
            )

        labels = {
            'weight': 'Weight', 'gl_level': 'Glucose level',
            # 'height': 'Height',
            'day': 'Day',
        }
        widgets = {
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kg(like 90.3)'}),
            'gl_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mg/dL'}),
            # 'height': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cm'}),
            'day': forms.TextInput(attrs={'class': 'form-control','placeholder': '2022-12-12'})

        }
