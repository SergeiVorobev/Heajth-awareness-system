# forms.py
from django import forms
from django.forms import ModelForm

from .models import QuestionaryModel
class QuestionaryForm(ModelForm):

    # def __init__(self, user, *args, **kwargs):
    #     self.user = user
    #     super(QuestionaryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = QuestionaryModel
        fields = (
            'on_a_diet', 'diet_meal_quantity',
            'phisical_exercises', 'physical_activity',
            # 'datetime'
            )

        labels = {
            'on_a_diet': 'Are you guided by a diet against diabetes?',
            'diet_meal_quantity': 'How often do you take a meal without a diet per week?',
            'phisical_exercises': 'Do you do physical exercises?',
            'physical_activity': 'Are you getting up and moving after 30 minutes sitting usually?',
            # 'datetime': 'date and time',
        }
        widgets = {
            'on_a_diet': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Yes/No', 'maxlength': 10}),
            'diet_meal_quantity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'How many'}),
            'phisical_exercises': forms.Select(attrs={'class': 'form-control', 'placeholder': 'How often'}),
            'physical_activity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Yes/No'}),
            # 'datetime' = forms.DateField(required=False),
        }
