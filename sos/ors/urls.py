from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test_sos),
    path('hello/', views.hello_world),
]
