"""Class models for suggestions package"""
from django.db import models
from django.utils.timezone import now


class DIET_CHOICES(models.TextChoices):
    ALWAYS = 'Always on diet'
    ONE_TIMES = '1 time'
    TWO_TIMES = '2 times'
    THREE_TIMES = '3 times'
    FOUR_TIMES = '4 times'
    NEVER = 'I have no any diet'

class PHYS_EXS(models.TextChoices):
    Yes_and_more_2_hours_per_week = 'Yes, and more then 2 hours per week'
    Yes_but_less_2_hours_per_week = 'Yes, but less then 2 hours per week'
    NO = 'No, I do not do any physical exercises'

class BOOLEAN_CHOICE(models.TextChoices):
    YES = 'Yes'
    NO = 'No'

class QuestionaryModel(models.Model):
    """Class model for questionary"""

    on_a_diet = models.CharField(max_length=3,
       choices=BOOLEAN_CHOICE.choices,
       default = "No")
    diet_meal_quantity = models.CharField(max_length=256,
       choices=DIET_CHOICES.choices,
       default = 'I have no any diet')
    phisical_exercises = models.CharField(max_length=256,
       choices=PHYS_EXS.choices,
       default = "No, I do not do any phisical exercises")
    physical_activity = models.CharField(max_length=3,
       choices=BOOLEAN_CHOICE.choices,
       default = "No")
    datetime = models.DateTimeField(default=now, editable=False)

    def save(self, *args, **kwargs):
        super().save(args, **kwargs)


class SuggestionModel(models.Model):
    points_max = models.IntegerField(default=20)
    points_achived = models.IntegerField(default=0)
    forecast = models.CharField(max_length=256, default = None)
    suggestion = models.CharField(max_length=256, default = None)

    @property
    def succes_result(self):
        return round(self.points_max/self.points_achived) 
 