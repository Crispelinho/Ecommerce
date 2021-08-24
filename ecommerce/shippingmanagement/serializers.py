from rest_framework import serializers
from shippingmanagement import models
from drf_base64.serializers import ModelSerializer

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shipment
        fields = "__all__"