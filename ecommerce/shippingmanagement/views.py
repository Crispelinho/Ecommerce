from django.shortcuts import render
from rest_framework import viewsets
from shippingmanagement.models import Shipment
from shippingmanagement.serializers import ShipmentSerializer

# Create your views here.
class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer