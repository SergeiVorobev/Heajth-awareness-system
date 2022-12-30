from django import forms

from .models import QuestionaryModel


class QuestionaryForm(forms.ModelForm):

    class Meta:
        model = QuestionaryModel
        fields = (
            'on_a_diet', 'diet_meal_quantity',
            'phisical_exercises', 'physical_activity',
            )

        labels = {
            'on_a_diet': 'Are you guided by a diet against diabetes?',
            'diet_meal_quantity': 'How often do you take a meal without a diet per week?',
            'phisical_exercises': 'Do you do physical exercises?',
            'physical_activity': 'Are you getting up and moving after 30 minutes sitting usually?',
        }
        widgets = {
            'on_a_diet': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Yes/No', 'maxlength': 10}),
            'diet_meal_quantity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'How many'}),
            'phisical_exercises': forms.Select(attrs={'class': 'form-control', 'placeholder': 'How often'}),
            'physical_activity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Yes/No'}),
        }
