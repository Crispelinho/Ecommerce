from django import forms
from .models import Order, Product, Payment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
        'name',
        'quantity',
        'unit_price',
        'state'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
            'quantity' : forms.TextInput(attrs={'class':'form-control' , 'type':'number'}),
            'unit_price' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'state'  : forms.Select(attrs={'class':'form-control'}) 
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
        'state',
        'payment_method',
        'shipment_address',
        'amount',
        'pending_amount'
        ]
        widgets = {
            'state' : forms.Select(attrs={'class':'form-control'}),
            'payment_method' : forms.Select(attrs={'class':'form-control'}),
            'shipment_address' : forms.TextInput(attrs={'class':'form-control'}),
            'amount' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'pending_amount' : forms.TextInput(attrs={'class':'form-control', 'type':'number'})
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
        'paymentmethod',
        'payment_value',
        ]
        widgets = {
            'paymentmethod' : forms.Select(attrs={'class':'form-control'}),
            'payment_value' : forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
        }