"""Define urls for suggestion package"""
from django.urls import path
from . import views

app_name = 'suggestions'

urlpatterns = [
    path('get-health-answers/', views.get_health_answers, name='get-health-answers'),
]

