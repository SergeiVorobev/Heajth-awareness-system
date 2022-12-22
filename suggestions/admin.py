"""Models Registration for Admin"""
from django.contrib import admin
from .models import QuestionaryModel, SuggestionModel
# CategoryQuestion, Question, Answer, Suggestion,

# # Register your models here.
# admin.site.register(CategoryQuestion)
# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Suggestion)
admin.site.register(QuestionaryModel)
admin.site.register(SuggestionModel)
