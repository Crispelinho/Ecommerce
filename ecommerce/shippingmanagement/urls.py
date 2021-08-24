from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from shippingmanagement.views import *
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'shipment', ShipmentViewSet)

urlpatterns = [
    path('', include(router.urls))

]