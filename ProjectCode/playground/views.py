from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import mysql.connector as sql
from django.contrib.auth import authenticate



fname=''
lname=''
email=''
pass1=''
fname=''
email1=''
pas11=''


def homeinit(request):
    return HttpResponse("Hello Maria's World")

def home(request):
    return render(request, 'index.html', {'name':'HomePage'})

def signout(request):
    pass

def signup(request):
    global fname, lname, email, pass1
    if request.method == "POST":
        m=sql.connect(host="localhost", user = "root", password="Mummy123daddy", database ="mariadb",auth_plugin='mysql_native_password')
        cursor = m.cursor()
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']  

        c= "insert into users Values('{}','{}','{}','{}')".format(fname,lname,email,pass1)
        cursor.execute(c)
        m.commit()
    return render(request, 'signup.html')

def signin(request):
    global email1,pass11
    if request.method=="POST":
        mm=sql.connect(host="localhost", user = "root", password="Mummy123daddy", database ="mariadb",auth_plugin='mysql_native_password')
        cursor = mm.cursor()
        email1 = request.POST['email']
        pass11 = request.POST['password']

        cc="select * from users where email= '{}'and password = '{}'".format(email1,pass11)
        cursor.execute(cc)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request, "Invalid email or password")
        else:
            return render(request, 'welcome.html')
    return render(request, 'signin.html')
