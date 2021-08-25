from rest_framework import serializers
from ordermanagement import models
from drf_base64.serializers import ModelSerializer
import requests, json
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
class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderPayment
        fields = "__all__"
class PaymentListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        paymentList=list()
        for item in validated_data:
            orderpayment_data = item.pop('orderpayment_set')
            payment = models.Payment.objects.create(**item)
            paymentList.append(payment.id)
            for pay_data in orderpayment_data:
                pay_data['payment'] = payment     
                orderpayments = models.OrderPayment.objects.create(**pay_data)                 
        return models.Payment.objects.filter(id__in=paymentList)       
class PaymentSerializer(serializers.ModelSerializer):
    orderpayment_set = OrderPaymentSerializer(many=True)
    class Meta:
        model = models.Payment
        list_serializer_class = PaymentListSerializer
        fields = "__all__"
    def create(self, validated_data):
        if validated_data['payment_value']>0:
            orderpayment_data = validated_data.pop('orderpayment_set')
            payment = models.Payment.objects.create(**validated_data)
            payment_value = payment.payment_value
            url = "https://api.ipify.org/?format=json"
            for pay_data in orderpayment_data:
                order = pay_data['order']
                # for product in order.orderproducts_set:
                #     requests.get(url)
                pending_amount = order.pending_amount
                payment_value = payment_value - pending_amount
                if payment_value >=0:
                    models.Order.objects.filter(id=order.id).update(state_id=2,pending_amount=0)
                else:
                    models.Order.objects.filter(id=order.id).update(pending_amount= (-payment_value) )
                    break
                pay_data['payment'] = payment
                orderpayments = models.OrderPayment.objects.create(**pay_data)   
            return payment
        

