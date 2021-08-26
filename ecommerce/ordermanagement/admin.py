from django.contrib import admin
from ordermanagement.models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=("id","name","quantity","unit_price","state")
    search_fields=("quantity","unit_price","state")
    list_filter=("name",)
    icon_name = 'person'
    list_per_page=10
class OrderAdmin(admin.ModelAdmin):
    list_display=("id","state","payment_method","shipment_address","amount","pending_amount","datetime_created","datetime_updated")
    search_fields=("state",)
    list_filter=("state",)
    icon_name = 'person'
    list_per_page=10
class OrderProductAdmin(admin.ModelAdmin):
    list_display=("id","product","order","quantity","unit_price")
    search_fields=("quantity","unit_price")
    list_filter=("id",)
    icon_name = 'person'
    list_per_page=10
class PaymentAdmin(admin.ModelAdmin):
    list_display=("id","paymentmethod","payment_value","datetime_payment")
    search_fields=("payment_value","datetime_payment")
    list_filter=("payment_value",)
    icon_name = 'person'
    list_per_page=10
class OrderPaymentAdmin(admin.ModelAdmin):
    list_display=("id","order","payment")
    search_fields=("id",)
    list_filter=("id",)
    icon_name = 'person'
    list_per_page=10

admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
admin.site.register(OrderPayment,OrderPaymentAdmin)