from django.urls import path
from . import views


#URLConf
urlpatterns = [
path('hello/',views.say_hello),
path('',views.home, name = "home"),
path('hello/signup/',views.signup, name = "signup"),
path('hello/signin/',views.signin, name = "signin"),
path('hello/signout/',views.signout, name = "signout"),

]