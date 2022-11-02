from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
def say_hello(request):
    x=1
    y=2
    #return HttpResponse("Hello Maria's World")
    return render(request, 'index.html', {'name':'Maria'})

def home(request):
    return render(request, 'index.html', {'name':'HomePage'})

def signout(request):
    pass

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        theuser = User.object.create_user(username,email, pass1)
        theuser.first_name= fname
        theuser.last_name= lname

        theuser.save()
        messages.success(request, "Account created Successfully")
        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')
