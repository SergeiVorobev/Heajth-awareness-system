from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class HealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    gl_level = models.IntegerField()
    height = models.IntegerField(default=180)
    day = models.DateField(default=now,
        editable=True
        )

    # @property
    def bmi_calculate(self):
        "Returns BMI index"
        return round(self.weight/((self.height/100)**2), 1)

    bmi = property(bmi_calculate)

    def __str__(self):
        return str(self.day)
    
    def save(self, *args, **kwargs):
        super().save(args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Health Data'

