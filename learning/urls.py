"""Define urls for learning package"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    list_cards,
    show_card,
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)

app_name = 'learning' 

urlpatterns = [
    path('', list_cards, name='list-cards'),
    path('show_card/<card_id>', show_card, name='show-card'),
    path('quiz/', QuizListView.as_view(), name='main-view'),
    path('quiz/<pk>/', quiz_view, name='quiz-view'),
    path('quiz/<pk>/save/', save_quiz_view, name='save-view'),
    path('quiz/<pk>/data/', quiz_data_view, name='quiz-data-view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

