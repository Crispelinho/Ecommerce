from django.db import models
from principal.models import PaymentMethod, StateOrder, StateProduct

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit_price = models.FloatField()
    state = models.ForeignKey(StateProduct, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)

class Order(models.Model):
    id = models.AutoField(primary_key = True)
    date = models.DateField()
    state = models.ForeignKey(StateOrder, blank=False, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, blank=False, on_delete=models.CASCADE)
    shipment_address = models.CharField(max_length=50)
    amount = models.FloatField()
    pending_amount = models.FloatField()
    order_product = models.ManyToManyField(Product, through='OrderProduct')
    datetime_created = models.DateTimeField('Fecha de creación de la orden',auto_now= False, auto_now_add = True)
    datetime_updated = models.DateTimeField('Fecha de actualización de la orden',auto_now= True, auto_now_add = False)
    def __str__(self):
        return (self.name)

class OrderProduct(models.Model):
    id = models.AutoField(primary_key = True)
    product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, blank=False, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit_price = models.FloatField()

class Payment(models.Model):
    id = models.AutoField(primary_key = True)
    paymentmethod = models.ForeignKey(PaymentMethod, blank=False, on_delete=models.CASCADE)
    payment_value = models.FloatField()
    datetime_payment = models.DateTimeField()

class OrderPayment(models.Model):
    id = models.AutoField(primary_key = True)
    order = models.ForeignKey(Order, blank=False, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, blank=False, on_delete=models.CASCADE)
    