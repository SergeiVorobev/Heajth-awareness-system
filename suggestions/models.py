"""Class models for suggestions package"""
from django.db import models

# Create your models here.
class CategoryQuestion(models.Model):
    """Class model for category question"""

    name = models.CharField(max_length=200)


class Question(models.Model):
    """Class model for question"""

    category = models.ForeignKey(CategoryQuestion, on_delete=models.CASCADE)
    name = models.TextField()


class Answer(models.Model):
    """Class model for answer"""

    # user = models.ForeignKey(User)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    poits = models.IntegerField()


class Suggestion(models.Model):
    """Class model for suggestion"""

    # user = models.ForeignKey(User)
    poits_sum = models.IntegerField()
    risk_prediction = models.TextField()
    suggestion = models.TextField()
