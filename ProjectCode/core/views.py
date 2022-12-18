from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
import mysql.connector as sql
from django.contrib.auth import authenticate

from .models import Profile
# Create your views here.

username=''
lname=''
email=''
pass1=''
pass2=''
fname=''
email1=''
pas11=''

def index(request):
    return render(request, 'index.html')
def signup(request):
    global username, email, pass1, pass2
    if request.method == "POST":
        m=sql.connect(host="localhost", user = "root", password="Mummy123daddy", database ="mariadb",auth_plugin='mysql_native_password')
        cursor = m.cursor()
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']  
        pass2 = request.POST['password2']  
        if pass1==pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username, email=email,password=pass2)
                c= "insert into users Values('{}','{}','{}','{}')".format(fname,email,pass1,pass2)
                cursor.execute(c)
                m.commit()
                user_model=User.objects.get(username=username)
                newprofile=Profile.objects.create(user=user_model, id_user=user_model.id)
                newprofile.save()
                user.save()
                user_login = auth.authenticate(username=username,password=pass1)
                auth.login(request, user_login)
                return redirect ('settings')

        else: 
            messages.info(request,"Passwords donot match")
    return render(request, 'signup.html')
def settings(request):
    # user_profile=Profile.objects.get(user=request.user)
    return render(request, 'setting.html')

def signin(request):
    global email1,pass11
    if request.method=="POST":
        mm=sql.connect(host="localhost", user = "root", password="Mummy123daddy", database ="mariadb",auth_plugin='mysql_native_password')
        cursor = mm.cursor()
        email1 = request.POST['username']
        pass11 = request.POST['password']

        cc="select * from users where email= '{}'and password = '{}'".format(email1,pass11)
        cursor.execute(cc)
        t=tuple(cursor.fetchall())
        if t==():
            messages.info(request, "Invalid email or password")
        else:
            return render(request, 'index.html')
    return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')