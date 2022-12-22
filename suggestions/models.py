"""Class models for suggestions package"""
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from user.models import Profile

# Create your models here.
# class CategoryQuestion(models.Model):
#     """Class model for category question"""

#     name = models.CharField(max_length=200)


# class Question(models.Model):
#     """Class model for question"""

#     category = models.ForeignKey(CategoryQuestion, on_delete=models.CASCADE)
#     name = models.TextField()


# class Answer(models.Model):
#     """Class model for answer"""

#     # user = models.ForeignKey(User)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.TextField()
#     poits = models.IntegerField()



# class Suggestion(models.Model):
#     """Class model for suggestion"""

#     user = models.ForeignKey(User)
#     poits_sum = models.IntegerField()
#     risk_prediction = models.TextField()
#     suggestion = models.TextField()


class DIET_CHOICES(models.TextChoices):
    ALWAYS = 'Always on diet'
    ONE_TIMES = '1 time'
    TWO_TIMES = '2 times'
    THREE_TIMES = '3 times'
    FOUR_TIMES = '4 times'
    NEVER = 'I have no any diet'

class PHYS_EXS(models.TextChoices):
    YES_MORE_2H_PER_WEEK = 'Yes, and more then 2 hours per week'
    YES_LESS_2H_PER_WEEK = 'Yes, but less then 2 hours per week'
    NO = 'No, I do not do any physical exercises'

class BOOLEAN_CHOICE(models.TextChoices):
    YES = 'Yes'
    NO = 'No'

class QuestionaryModel(models.Model):
    """Class model for questionary"""

    # user = models.ForeignKey(User, on_delete=models.PROTECT)
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
    # user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    points_max = models.IntegerField(default=20)
    points_achived = models.IntegerField(default=0)
    forecast = models.CharField(max_length=256, default = None)
    suggestion = models.CharField(max_length=256, default = None)

    @property
    def succes_result(self):
        return round(self.points_max/self.points_achived) 
 