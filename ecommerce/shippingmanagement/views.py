from django.shortcuts import render
from django.template import loader
from rest_framework import viewsets
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from shippingmanagement.models import *
from shippingmanagement.serializers import ShipmentSerializer
from shippingmanagement.forms import ShipmentForm
from principal.models import *
from ordermanagement.models import *
from django.core.mail import EmailMessage
from django.conf import settings 
import json

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
    context ={}
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if ('state' in request.POST) or ('order' in request.POST):
            form.save()
            return HttpResponseRedirect('/shipment/')
        elif 'delete' in request.POST:
            data=json.loads(request.POST['delete'])
            if data:
                id = data['id']
                print(id)
                Shipment.objects.filter(id=id).delete()
        elif 'editar' in request.POST:
            data=json.loads(request.POST['editar'])
            id = data['id']
            fields = data['detalleArray']
            print('editar',fields)
            print(request.user.id)
            orderShipment = fields['orderShipment']
            shipment_address = fields['shipment_address']
            Order.objects.filter(id=orderShipment).update(shipment_address=shipment_address)
        else:
            return HttpResponseRedirect('/Error/')
    else:   
            form = ShipmentForm()
            context ={'form': form,
            'shipments': Shipment.objects.all(),
            'states':StateShipment.objects.all(),
            'stateorders':StateOrder.objects.all(),
            'paymentmethods':PaymentMethod.objects.all(),
            'orders':Order.objects.all()
            }
    return HttpResponse(template.render(context, request))