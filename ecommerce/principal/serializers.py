from rest_framework import serializers
from principal import models
from drf_base64.serializers import ModelSerializer

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentMethod
        fields = "__all__"

class StateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StateProduct
        fields = "__all__"

class StateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StateOrder
        fields = "__all__"

class StateShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StateShipment
        fields = "__all__"