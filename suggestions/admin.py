"""Models Registration for Admin"""
from django.contrib import admin
from .models import CategoryQuestion, Question, Answer, Suggestion

# Register your models here.
admin.site.register(CategoryQuestion)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Suggestion)
