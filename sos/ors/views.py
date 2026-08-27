from django.http import HttpResponse
from django.shortcuts import render
from django.middleware.csrf import get_token


def test_ors(request):
    return HttpResponse("Hello, world.")
def hello_world(request):
    return HttpResponse("Hello Man")

def user_signup(request):
    token = get_token(request)
    print(request.POST.get('firstName'))
    print(request.POST.get('lastName'))
    print(request.POST.get('loginId'))
    print(request.POST.get('password'))
    print(request.POST.get('dob'))
    print(request.POST.get('address'))
    print("Token is ",token)




    return render(request, 'UserRegistration.html')
