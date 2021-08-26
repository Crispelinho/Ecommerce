from django import forms
from .models import Shipment
# from .models import Ruta
# from .models import Dominical
# from .models import Cargo
# from .models import Empleado
# from django.contrib.admin import widgets

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = [
        'departure_datetime',
        'state',
        'order'
        ]
        widgets = {
            'departure_datetime': forms.DateInput(attrs={'class':'form-control', 'type':'datetime-local'}),
            'state' : forms.Select(attrs={'class':'form-control'}),
            'order' : forms.Select(attrs={'class':'form-control'}),
        }