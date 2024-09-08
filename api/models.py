from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os
# Create your models here.


class Fisherman(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_num = models.IntegerField()
    

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



class FishermenRegistration(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Fishermen')
    address = models.TextField()
    
    
    

class VesselRegistration(models.Model):
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Fishermen')
    business_address = models.TextField()
    year_built = models.DateField()
    length = models.TextField()
    breadth = models.TextField()
    depth = models.TextField()
    draught = models.TextField()
    gross = models.TextField()
    net = models.TextField()
    hull_material = models.TextField()
    mast = models.TextField()
    color = models.TextField()
    stern = models.TextField()
    crew_num = models.TextField()
    serial_num = models.TextField()
    cycle = models.TextField()
    cylander_num = models.TextField()
    engine_num = models.TextField()
    former_owner = models.TextField()
    address = models.TextField()
    
class FishingPermit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Fishermen')
    address = models.TextField()
    home_port = models.TextField()
    vessel_name = models.TextField()
    vessel_type = models.TextField()
    color = models.TextField()
    service_type = models.TextField()
    description = models.TextField()
    length = models.TextField()
    breadth = models.TextField()
    depth = models.TextField()
    draught = models.TextField()
    gross = models.TextField()
    net = models.TextField()
    engine = models.TextField()
    serial_num = models.TextField()
    horse_power = models.TextField()
    cylinder_num = models.TextField()
    engine_num = models.TextField()
    crew_num = models.TextField()
    coast_guard_num = models.TextField()
    mfvr_num = models.TextField()