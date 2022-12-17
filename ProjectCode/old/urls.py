from django.urls import path
from . import views


#URLConf
urlpatterns = [
#path('hello/',views.say_hello),
path('',views.home, name = "home"),
path('signup/',views.signup, name = "signup"),
path('signin/',views.signin, name = "signin"),
path('resetpassword/',views.resetpassword, name = "resetpassword"),
path('resetdone/',views.resetdone, name = "resetdone"),
path('myspace/',views.myspace, name = "myspace"),
path('friendspace/',views.friendspace, name = "friendspace"),
path('chatroom/',views.chatroom, name = "chatroom"),
path('settings/',views.settings, name = "settings"),
path('ContactUs/',views.ContactUs, name = "ContactUs"),
path('welcome/',views.welcome, name = "welcome"),
path('upload/',views.upload, name = "upload"),
 

#path('signout/',views.signout, name = "signout"),


]