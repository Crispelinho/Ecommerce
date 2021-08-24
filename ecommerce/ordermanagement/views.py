from django.shortcuts import render
from rest_framework import viewsets
from ordermanagement.models import Product, Order, OrderProduct, Payment, OrderPayment
from ordermanagement.serializers import ProductSerializer, OrderSerializer, OrderProductSerializer, PaymentSerializer, OrderPaymentSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class OrderPaymentViewSet(viewsets.ModelViewSet):
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer