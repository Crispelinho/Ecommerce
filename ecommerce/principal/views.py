from django.shortcuts import render
from rest_framework import viewsets
from principal.models import PaymentMethod, StateProduct, StateOrder, StateShipment
from principal.serializers import PaymentMethodSerializer, StateProductSerializer, StateOrderSerializer, StateShipmentSerializer

# Create your views here.

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class StateProductViewSet(viewsets.ModelViewSet):
    queryset = StateProduct.objects.all()
    serializer_class = StateProductSerializer

class StateOrderViewSet(viewsets.ModelViewSet):
    queryset = StateOrder.objects.all()
    serializer_class = StateOrderSerializer

class StateShipmentViewSet(viewsets.ModelViewSet):
    queryset = StateShipment.objects.all()
    serializer_class = StateShipmentSerializer