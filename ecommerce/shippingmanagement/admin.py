from django.contrib import admin
from shippingmanagement.models import *
# Register your models here.
class ShipmentAdmin(admin.ModelAdmin):
    list_display=("id","departure_datetime","state","order")
    search_fields=("departure_datetime","state")
    list_filter=("state",)
    icon_name = 'person'
    list_per_page=10

admin.site.register(Shipment,ShipmentAdmin)