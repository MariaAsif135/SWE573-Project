from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import mysql.connector as sql


def homeinit(request):
    return HttpResponse("Hello Maria's World")

def home(request):
    return render(request, 'index.html', {'name':'HomePage'})

def signout(request):
    pass

def signup(request):
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
    return render(request, 'signin.html')

def signin(request):
    return render(request, 'signin.html')
