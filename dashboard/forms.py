from django import forms

from .models import HealthData


class DateInput(forms.DateInput):
    input_type = 'date'


class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ('weight', 'gl_level', 'height', 'day')

        labels = {
            'weight': 'Weight', 'gl_level': 'Glucose level',
            'height': 'Height',
            'day': 'Day',
        }
        widgets = {
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kg(like 90.3)'}),
            'gl_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mg/dL'}),
            'height': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cm'}),
            'day': forms.DateInput(),
        }
