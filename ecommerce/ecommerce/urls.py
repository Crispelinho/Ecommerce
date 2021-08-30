"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from ordermanagement.views import *
from shippingmanagement.views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
     path('', ProductFormView),
     path('principal/', include('principal.urls')),
     path('ordermanagement/', include('ordermanagement.urls')),
     path('shippingmanagement/', include('shippingmanagement.urls')),
     path('product/', ProductFormView, name='product'),
     path('order/', OrderFormView, name='order'),    
     path('shipment/', ShipmentFormView, name='shipment'), 
     path('payment/', PaymentFormView),  
    #  path('admin/',ProductFormView, name='admin'),
     url(r'^api-token-auth/', obtain_jwt_token),
     path('admin/', admin.site.urls, name='admin'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)