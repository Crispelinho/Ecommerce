from django.contrib import admin
from shippingmanagement.models import *
from django.contrib.admin import AdminSite

# Register your models here.
class ShipmentAdmin(admin.ModelAdmin):
    list_display=("id","departure_datetime","state","order")
    search_fields=("departure_datetime","state")
    list_filter=("state",)
    icon_name = 'person'
    list_per_page=10

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'
    admin.site.site_header = "Portal de Administración Principal - eCommerce"
    admin.site.index_title = "Bienvenidos al portal de administración"
admin_site = MyAdminSite(name='myadmin')

admin.site.register(Shipment,ShipmentAdmin)