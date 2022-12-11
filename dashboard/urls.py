"""Define urls for dashboard package"""
from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    # path('', views.home, name="users-home"),
    path('add-health-data/', views.add_health_data, name='add-health-data'),
]

