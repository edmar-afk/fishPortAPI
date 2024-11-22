from django.contrib import admin
from .models import FishingPermit, VesselRegistration, ExpirationDate


admin.site.register(FishingPermit)
admin.site.register(VesselRegistration)
admin.site.register(ExpirationDate)