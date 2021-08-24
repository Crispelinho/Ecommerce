from rest_framework import serializers
from ordermanagement import models
from drf_base64.serializers import ModelSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderProduct
        fields = "__all__"

class OrderListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        orderList=list()
        for item in validated_data:
            orderproducts_data = item.pop('orderproduct_set')
            order = models.Order.objects.create(**item)
            orderList.append(order.id)
            for or_data in orderproducts_data:
                or_data['order'] = order
                orderproducts = models.OrderProduct.objects.create(**or_data)                 
        return models.Order.objects.filter(id__in=orderList)
    
class OrderSerializer(serializers.ModelSerializer):
    orderproduct_set = OrderProductSerializer(many=True)
    class Meta:
        model = models.Order
        list_serializer_class = OrderListSerializer
        fields = "__all__"
    def create(self, validated_data):
        orderproducts_data = validated_data.pop('orderproduct_set')
        order = models.Order.objects.create(**validated_data)
        for or_data in orderproducts_data:
            or_data['order'] = order
            orderproducts = models.OrderProduct.objects.create(**or_data)   
        return order
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = "__all__"

class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderPayment
        fields = "__all__"
