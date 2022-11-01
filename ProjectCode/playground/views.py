from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    x=1
    y=2
    #return HttpResponse("Hello Maria's World")
    return render(request, 'index.html', {'name':'Maria'})

def home(request):
    return HttpResponse("Hello I am working")

def signout(request):
    pass

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')
