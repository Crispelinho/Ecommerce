from django.shortcuts import render
from rest_framework import viewsets
from shippingmanagement.models import Shipment
from shippingmanagement.serializers import ShipmentSerializer
from django.core.mail import EmailMessage
from django.conf import settings 
# Create your views here.

def send_email(subjectReceived, bodyRequest, emails):
    email = EmailMessage(
        subjectReceived,
        bodyRequest,
        settings.EMAIL_HOST_USER,
        emails,
    )
    email.send()  
class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer