from django.db import models
from principal.models import StateShipment
from ordermanagement.models import Order
from django.contrib.auth.models import User

# Create your models here.
class Shipment(models.Model):
    id = models.AutoField(primary_key = True)
    departure_datetime = models.DateTimeField(max_length=50)
    state = models.ForeignKey(StateShipment, blank=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.id))

class Request(models.Model):
    id = models.AutoField(primary_key = True)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.CharField(max_length=2000, blank=False, null=False)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.subject)
    class Meta:
        get_latest_by = 'id'