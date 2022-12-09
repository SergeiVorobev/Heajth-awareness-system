"""Define urls for learning package"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'learning' 

urlpatterns = [
    path('', views.list_cards, name='list-cards')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

