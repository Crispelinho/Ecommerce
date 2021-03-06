from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from ordermanagement.views import *
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename="products")
router.register(r'order', OrderViewSet, basename="orders")
router.register(r'orderProduct', OrderProductViewSet)
router.register(r'payment', PaymentViewSet,basename="payments")
router.register(r'oredePayment', OrderPaymentViewSet)

urlpatterns = [
    path('', include(router.urls))
]