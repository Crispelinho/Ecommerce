from rest_framework import serializers
from ordermanagement import models
from drf_base64.serializers import ModelSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderProduct
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = "__all__"

class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderPayment
        fields = "__all__"
