from rest_framework import serializers
from shippingmanagement import models
from drf_base64.serializers import ModelSerializer
from ordermanagement.serializers import OrderSerializer
class ShipmentSerializer(serializers.ModelSerializer):
    # order = OrderSerializer(read_only=True)
    class Meta:
        model = models.Shipment
        fields = "__all__"
    