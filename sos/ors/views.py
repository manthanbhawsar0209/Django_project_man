from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.middleware.csrf import get_token
from .service.UserService import UserService
from django.contrib.sessions.models import Session

def test_ors(request):
    return HttpResponse("Hello, world.")
def hello_world(request):
    return HttpResponse("Hello Man")
def welcome(request):
    return render(request,"Welcome.html")
def user_signup(request):
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
    # token = get_token(request)
    # print(request.POST.get('firstName'))
    # print(request.POST.get('lastName'))
    # print(request.POST.get('loginId'))
    # print(request.POST.get('password'))
    # print(request.POST.get('dob'))
    # print(request.POST.get('address'))
    # print("Token is ",token)

    return render(request, 'UserRegistration.html')

def user_login(request):
    message = ''
    if request.method == "POST":
        loginId = request.POST.get('loginId')
        password = request.POST.get('password')
        service = UserService()
        user_data = service.auth(loginId, password)
        if len(user_data) != 0:
            request.session['firstName'] = user_data[0].get('firstName')
            return redirect('/ors/welcome')
            # return render(request, 'Welcome.html', {'firstName': user_data[0].get('firstName')})
        else:
            message = 'login & password is invalid'
    return render(request, 'Login.html', {'message': message})

def logout(request):
    request.session['firstName'] = None
    return redirect('/ors/login')

def create_session(request):
    request.session['name'] = 'Admin'
    response = "<h1>Welcome To Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)

def access_session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)

def destroy_session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")

def setCookies(request):
    key = "name"
    value = "abc"
    res = HttpResponse("<h1>cookie created..!!</h1>")
    res.set_cookie(key, value, max_age=20)
    return res

def getCookies(request):
    value = request.COOKIES.get('name')
    html = "<h3><center> value = {} </center></h3>".format(value)
    return HttpResponse(html)

def user_save(request):
    message = ''
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        if request.POST['operation'] == "save":
            service.add(params)
            message = 'User Added Successfully'
        if request.POST['operation'] == "update":
            params['id'] = request.POST.get('id')
            service.update(params)
            message = 'User Updated Successfully'
    return render(request, 'User.html', {'message': message})

def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}
    ]
    return render(request, "TestList.html", {"list": list})