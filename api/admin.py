from django.contrib import admin
from .models import FishingPermit, VesselRegistration, ExpirationDate, PermitExpirationDate, WeighIn


admin.site.register(FishingPermit)
admin.site.register(VesselRegistration)
admin.site.register(ExpirationDate)
admin.site.register(PermitExpirationDate)
@admin.register(WeighIn)
class WeighInAdmin(admin.ModelAdmin):
    list_display = ('fish', 'price_per_kilo', 'kg', 'total_price', 'date_weighin')  # Include date_weighin