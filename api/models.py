from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os
# Create your models here.

class FishType(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
    
class WeighIn(models.Model):
    fish = models.ForeignKey(FishType, on_delete=models.CASCADE)
    price_per_kilo = models.TextField()
    kg = models.TextField()
    total_price = models.TextField()
    date_weighin = models.DateTimeField(auto_now_add=True)