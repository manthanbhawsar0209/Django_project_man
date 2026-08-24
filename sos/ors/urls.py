from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test_ors),
    path('hello/', views.hello_world),
    path('signup/', views.user_signup),
]
