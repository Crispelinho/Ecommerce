from django.db import models
from principal.models import StateShipment
from ordermanagement.models import Order
# Create your models here.
class Shipment(models.Model):
    id = models.AutoField(primary_key = True)
    departure_datetime = models.DateTimeField(max_length=50)
    state = models.ForeignKey(StateShipment, blank=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)