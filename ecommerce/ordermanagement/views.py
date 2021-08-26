from django.shortcuts import render
from django.template import loader
from rest_framework import viewsets
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ordermanagement.models import Product, Order, OrderProduct, Payment, OrderPayment
from ordermanagement.serializers import ProductSerializer, OrderSerializer, OrderProductSerializer, PaymentSerializer, OrderPaymentSerializer
from ordermanagement.forms import ProductForm, OrderForm, PaymentForm
from principal.models import *

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
            print(data)
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
    template = loader.get_template('product.html')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product/')
        else:
            return HttpResponseRedirect('/Error/')
    else:   
            form = ProductForm()
            context ={'form': form,
            'products': Product.objects.all(),
            'states':StateProduct.objects.all(),
            }
    return HttpResponse(template.render(context, request))

def OrderFormView(request):
    template = loader.get_template('order.html')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/order/')
        else:
            return HttpResponseRedirect('/Error/')
    else:   
            form = OrderForm()
            context ={'form': form,
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
            datetime_payment = data['datetime_payment']
            orderPayment = Order.objects.filter(id=data['orderPayment']).first() 
            Payment.objects.create(paymentmethod=paymentmethod,payment_value=payment_value,datetime_payment=datetime_payment)
            lastEntrada=Payment.objects.last()
            print('pay: ',lastEntrada.id)
            pay = Payment.objects.filter(id=lastEntrada.id).first()
            OrderPayment.objects.create(order=orderPayment,payment=pay)
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