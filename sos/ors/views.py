from django.http import HttpResponse

def test_sos(request):
    return HttpResponse("Hello, world.")
def hello_world(request):
    return HttpResponse("Hello Man")