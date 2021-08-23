from django.db import models

# Create your models here.
class PaymentMethod(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    decription = models.CharField(max_length=50)
    def __str__(self):
        return (self.name)

class StateProduct(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    def __str__(self):
        return (self.name)

class StateOrder(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    def __str__(self):
        return (self.name)

class StateShipment(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    def __str__(self):
        return (self.name)