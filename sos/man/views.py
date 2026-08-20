from django.http import HttpResponse


def test_sos(request):
    return HttpResponse("Hello, Man")


def hello_world(request):
    return HttpResponse("Hello Man")


from django.shortcuts import render

# Create your views here.
