from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test_ors),
    path('hello/', views.hello_world),
    path('signup/', views.user_signup),
    path('welcome/', views.welcome),
    path('', views.welcome),
    path('login/', views.user_login),
    path('logout/', views.logout),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('destroy/', views.destroy_session),
    path('get/', views.getCookies),
    path('set/', views.setCookies),
    path('save/', views.user_save),
    path('testlist/', views.test_list),

]
