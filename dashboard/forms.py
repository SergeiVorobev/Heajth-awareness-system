from django import forms
from .models import HealthData
from django.forms import ModelForm

class HealthDataForm(ModelForm):
    class Meta:
        model = HealthData
        fields = (
            'weight', 'gl_level')

        labels = {
            'weight': 'Weight', 'gl_level': 'Glucose level',
        }
        widgets = {
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kg(like 90.3)'}),
            'gl_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mg/dL'})
        }
