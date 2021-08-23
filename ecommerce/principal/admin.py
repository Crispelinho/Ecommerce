from django.contrib import admin
from django.contrib.admin import AdminSite
from principal.models import *

# Register your models here.
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display=("id","name","description")
    search_fields=("name","description")
    list_filter=("name",)
    icon_name = 'person'
    list_per_page=10
class StateProductAdmin(admin.ModelAdmin):
    list_display=("id","name","description")
    search_fields=("name","description")
    list_filter=("name",)
    icon_name = 'person'
    list_per_page=10
class StateOrderAdmin(admin.ModelAdmin):
    list_display=("id","name","description")
    search_fields=("name","description")
    list_filter=("name",)
    icon_name = 'person'
    list_per_page=10
class StateShipmentAdmin(admin.ModelAdmin):
    list_display=("id","name","description")
    search_fields=("name","description")
    list_filter=("name",)
    icon_name = 'person'
    list_per_page=10

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'
    admin.site.site_header = "Portal de Administración Principal - eCommerce"
    admin.site.index_title = "Bienvenidos al portal de administración"
admin_site = MyAdminSite(name='myadmin')

admin.site.register(PaymentMethod,PaymentMethodAdmin)
admin.site.register(StateProduct,StateProductAdmin)
admin.site.register(StateOrder,StateOrderAdmin)
admin.site.register(StateShipment,StateShipmentAdmin)