from rest_framework import serializers
from shippingmanagement import models
from shippingmanagement import views

from drf_base64.serializers import ModelSerializer
from ordermanagement.serializers import OrderSerializer

class ShipmentSerializer(serializers.ModelSerializer):
    # order = OrderSerializer(read_only=True)
    class Meta:
        model = models.Shipment
        fields = "__all__"
    def create(self, validated_data):
        shipment = models.Shipment.objects.create(**validated_data)
        body = "Pedido "+str(shipment)+ " relacionado con la orden "+str(validated_data['order'].id)+"."
        models.Request.objects.create(subject="Envío de pedido", message=body, user = validated_data['order'].user)
        views.send_email("Envío de pedido",body,[validated_data['order'].user.email])
        return shipment