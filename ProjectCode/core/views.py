from itertools import chain
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
import mysql.connector as sql
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, Profile,LikePost
# Create your views here.

username=''
email=''
pass1=''
pass2=''
username1=''
pass11=''


def profile(request,pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    # if FollowersCount.objects.filter(follower=follower, user=user).first():
    #     button_text = 'Unfollow'
    # else:
    #     button_text = 'Follow'

    # user_followers = len(FollowersCount.objects.filter(user=pk))
    # user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        # 'button_text': button_text,
        # 'user_followers': user_followers,
        # 'user_following': user_following,
    }
    return render(request, 'profile.html', context)
# @login_required(login_url='core.signin')
def index(request):
    user_object=User.objects.get(username=request.user.username)
    user_profile= Profile.objects.get(user=user_object)

    posts=Post.objects.all()
    return render(request, 'index.html',{'user_profile': user_profile,'posts':posts})


def signup(request):
    global username, email, pass1, pass2
    if request.method == "POST":
       # m=sql.connect(host="localhost", user = "root", password="Mummy123daddy", database ="mariadb")
        m=sql.connect(host="mysql_db", user = "root", password="", database ="django")

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
                user=User.objects.create_user(username=username, email=email,password=pass1)
                c="insert into users Values('{}','{}','{}','{}')".format(username,email,pass1,pass2)
                cursor.execute(c)
                m.commit()
                user_model=User.objects.get(username=username)
                newprofile=Profile.objects.create(user=user_model, id_user=user_model.id)
                newprofile.save()
                user.save()
                user_login = auth.authenticate(username=user_model,password=pass1)
                auth.login(request, user_login)
                return redirect ('settings')
        else: 
            messages.info(request,"Passwords do not match")
    return render(request, 'signup.html')
    
def settings(request):
    user_profile= Profile.objects.get(user=request.user)
    return render(request, 'setting.html',{'user_profile':user_profile})


def signin(request):
    global username1,pass11
    if request.method=="POST":
        #mm=sql.connect(host="localhost", user = "root", password="Mummy123daddy", database ="mariadb")
        mm=sql.connect(host="mysql_db", user = "root", password="", database ="django")
        cursor = mm.cursor()
        username1 = request.POST['username']
        pass11 = request.POST['password']
        user = auth.authenticate(username=username1, password=pass11)
        cc="select * from users where FullName= '{}'and Password = '{}'".format(username1,pass11)
        cursor.execute(cc)
        t=tuple(cursor.fetchall())
        if t==():
            messages.info(request, "Invalid email or password")
        else:
            auth.login(request, user)
            return render(request, 'index.html')

    return render(request, 'signin.html')



def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})





def logout(request):
    auth.logout(request)
    return redirect('signin')

def welcome(request):
    return render(request, 'welcome.html')

def upload(request):
    if request.method == 'POST':
        user = request.user.username
        Link = request.POST['link']
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, Link=Link, caption=caption)
        new_post.save()


        return redirect ('/')
    else:
        return redirect('/')


def LikingPost(request):
    username=request.user.username
    post_id=request.GET.get('post_id')

    post=Post.objects.get(id=post_id)
    likingFilter=LikePost.objects.filter(post_id=post_id, username=username).first()

    if likingFilter==None:
        newlike=LikePost.objects.create(post_id=post_id, username=username)
        newlike.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        likingFilter.delete()
        post.no_of_likes=post.no_of_likes-1
        post.save()
        return redirect('/')

