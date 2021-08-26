from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from principal.views import *
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'paymentMethod', PaymentMethodViewSet)
router.register(r'stateProduct', StateProductViewSet)
router.register(r'stateOrder', StateOrderViewSet)
router.register(r'stateShipment', StateShipmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]