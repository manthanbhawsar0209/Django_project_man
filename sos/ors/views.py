from django.http import HttpResponse
from django.shortcuts import render

def test_ors(request):
    return HttpResponse("Hello, world.")
def hello_world(request):
    return HttpResponse("Hello Man")
def user_signup(request):
    return render(request, 'UserRegistration.html')