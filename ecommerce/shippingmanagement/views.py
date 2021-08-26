from django.shortcuts import render
from django.template import loader
from rest_framework import viewsets
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from shippingmanagement.models import Shipment
from shippingmanagement.serializers import ShipmentSerializer
from shippingmanagement.forms import ShipmentForm
from principal.models import StateShipment
from ordermanagement.models import Order
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

def ShipmentFormView(request):
    template = loader.get_template('Shipment.html')
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/shipment/')
        else:
            return HttpResponseRedirect('/Error/')
    else:   
            form = ShipmentForm()
            context ={'form': form,
            'shipments': Shipment.objects.all(),
            'states':StateShipment.objects.all(),
            'orders':Order.objects.all()
            }
    return HttpResponse(template.render(context, request))