from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class HealthData(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    gl_level = models.IntegerField()
    daytime = models.DateTimeField(default=now, editable=False)
