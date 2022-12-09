"""Views for learning package"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Material

# Create your views here.
@login_required(login_url='user:login')
def list_cards(request):
    cards = Material.objects.all().order_by('created_date')
    return render(request, 'learning/base.html', {"cards": cards})