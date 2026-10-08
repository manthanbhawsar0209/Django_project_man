from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test_sos),
    path('hello/', views.hello_world),
    path('ors/', include('ors.urls')),
    path('man/', include('man.urls')),
    path('josh/', include('josh.urls')),
    path('', include('ors.urls')),
]
