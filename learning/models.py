"""Define models for learning package"""
from django.db import models

# Create your models here.

class Material(models.Model):
    """Define data for Material model"""

    name = models.CharField(max_length=100)
    img = models.ImageField()
    description = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
    