from django.shortcuts import render
from django.template import loader
from rest_framework import viewsets
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ordermanagement.models import Product, Order, OrderProduct, Payment, OrderPayment
from ordermanagement.serializers import ProductSerializer, OrderSerializer, OrderProductSerializer, PaymentSerializer, OrderPaymentSerializer
from ordermanagement.forms import ProductForm, OrderForm, PaymentForm
from principal.models import *
import json
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get_serializer(self, *args, **kwargs):
        if self.request.method.lower() == 'post':
            data = kwargs.get('data')
            kwargs['many'] = isinstance(data, list)
        return super(OrderViewSet, self).get_serializer(*args, **kwargs)
class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    def get_serializer(self, *args, **kwargs):
        if self.request.method.lower() == 'post':
            data = kwargs.get('data')
            kwargs['many'] = isinstance(data, list)
        return super(PaymentViewSet, self).get_serializer(*args, **kwargs)
class OrderPaymentViewSet(viewsets.ModelViewSet):
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer

def ProductFormView(request):
    # template = loader.get_template('product.html')
    if request.method == 'POST':
        context = {}
        form = ProductForm(request.POST)
        if ('name' in request.POST) or ('quantity' in request.POST):
            form.save()
            return HttpResponseRedirect('/product/')
        elif 'data' in request.POST:
            data=json.loads(request.POST['data'])
            if data:
                id = data['id']
                print(id)
                Product.objects.filter(id=id).delete()
            return HttpResponseRedirect('/product/')
        elif 'editar' in request.POST:
            data=json.loads(request.POST['editar'])
            id = data['id']
            fields = data['detalleArray']
            print('editar',fields)
            name = fields['name']
            quantity = fields['quantity']
            unit_price = fields['unit_price']
            state = fields['state']
            state = StateProduct.objects.filter(id=state).first()
            Product.objects.filter(id=id).update(name=name,quantity=quantity,unit_price=unit_price,state=state)
            return HttpResponseRedirect('/order/')
        else:
            return HttpResponseRedirect('/Error/')
    else:   
            form = ProductForm()
            context ={'form': form,
            'products': Product.objects.all(),
            'states':StateProduct.objects.all(),
            }
    return render(request, "product.html", context)

def OrderFormView(request):
    template = loader.get_template('order.html')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if ('payment_method' in request.POST) or ('pending_amount' in request.POST):
            if form.is_valid():   
                form.save()
            return HttpResponseRedirect('/order/')
        elif 'delete' in request.POST:
            data=json.loads(request.POST['delete'])
            if data:
                id = data['id']
                print(id)
                Order.objects.filter(id=id).delete()
            return HttpResponseRedirect('/order/')
        elif 'editar' in request.POST:
            data=json.loads(request.POST['editar'])
            id = data['id']
            fields = data['detalleArray']
            state = StateOrder.objects.filter(id=fields['state']).first()
            payment_method = PaymentMethod.objects.filter(id=fields['payment_method']).first()
            amount = fields['amount']
            pending_amount = fields['pending_amount']
            shipment_address = fields['shipment_address']
            Order.objects.filter(id=id).update(state=state,payment_method=payment_method,amount=amount,pending_amount=pending_amount,shipment_address=shipment_address)
            return HttpResponseRedirect('/order/')
        else:
            return HttpResponseRedirect('/Error/')
    else:   
            form = OrderForm()
            context ={'form': form,
            'user': {'idUser':request.user.id, 'user':request.user},
            'orders': Order.objects.all(),
            'states':StateOrder.objects.all(),
            'paymentMethods':PaymentMethod.objects.all()
            }
    return HttpResponse(template.render(context, request))

def PaymentFormView(request):
    template = loader.get_template('payment.html')
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        # form = PaymentForm(request.POST)
        if data:
            paymentmethod = PaymentMethod.objects.filter(id=data['payment_method']).first()
            payment_value = data['payment_value']
            orderPayment = Order.objects.filter(id=data['orderPayment'])
            Payment.objects.create(paymentmethod=paymentmethod,payment_value=payment_value)
            orderPayment.update(pending_amount=orderPayment.first().amount - float(payment_value))
            lastEntrada=Payment.objects.last()
            print('pay: ',lastEntrada.id)
            pay = Payment.objects.filter(id=lastEntrada.id).first()
            OrderPayment.objects.create(order=orderPayment.first(),payment=pay)
            return HttpResponseRedirect('/payment/')
        else:
            return HttpResponseRedirect('/Error/')
    else:   
            form = PaymentForm()
            context ={'form': form,
            'orderpayments': OrderPayment.objects.all(),
            'paymentMethods':PaymentMethod.objects.all(),
            'orders':Order.objects.all()
            }
    return HttpResponse(template.render(context, request))