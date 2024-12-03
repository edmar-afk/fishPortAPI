from django.contrib import admin
from .models import FishingPermit, VesselRegistration, ExpirationDate, PermitExpirationDate, WeighIn


admin.site.register(FishingPermit)
admin.site.register(VesselRegistration)
admin.site.register(ExpirationDate)
admin.site.register(PermitExpirationDate)
admin.site.register(WeighIn)