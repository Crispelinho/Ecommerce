from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from principal.views import *
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls)
]