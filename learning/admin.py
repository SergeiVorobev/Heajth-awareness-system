"""Models registration for Admin"""
from django.contrib import admin
from .models import Material

# Register your models here.
admin.site.register(Material)
