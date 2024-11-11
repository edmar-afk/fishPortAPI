from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

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
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fishermen_registrations')
    address = models.TextField()

class VesselRegistration(models.Model):
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vessel_registrations')
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fishing_permits')
    owner_name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    home_port = models.CharField(max_length=255, blank=True)
    vessel_name = models.CharField(max_length=255, blank=True)
    vessel_type = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=100, blank=True)
    service_type = models.CharField(max_length=100, blank=True)
    vessel_description = models.TextField(blank=True)  # Added field for vessel description
    
    # Changed numerical fields to CharField
    length = models.CharField(max_length=255, blank=True, null=True)
    breadth = models.CharField(max_length=255, blank=True, null=True)
    depth = models.CharField(max_length=255, blank=True, null=True)
    draught = models.CharField(max_length=255, blank=True, null=True)
    gross = models.CharField(max_length=255, blank=True, null=True)
    net = models.CharField(max_length=255, blank=True, null=True)
    
    engine = models.CharField(max_length=255, blank=True)
    serial_num = models.CharField(max_length=255, blank=True)
    horse_power = models.CharField(max_length=255, blank=True, null=True)  # Changed to CharField
    cylinder_num = models.CharField(max_length=255, blank=True, null=True)  # Changed to CharField
    engine_num = models.CharField(max_length=255, blank=True)
    crew_num = models.CharField(max_length=255, blank=True, null=True)  # Changed to CharField
    coast_guard_num = models.CharField(max_length=255, blank=True)
    mfvr_num = models.CharField(max_length=255, blank=True)
    or_num = models.CharField(max_length=255, blank=True)
    date_issued = models.DateField(blank=True)
    amount = models.TextField(blank=True)
    fishing_gear_used = models.TextField(blank=True)
    def __str__(self):
        return f"Fishing Permit for {self.vessel_name} owned by {self.owner_name}"



