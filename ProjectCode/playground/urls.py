from django.urls import path
from . import views


#URLConf
urlpatterns = [
#path('hello/',views.say_hello),
path('',views.home, name = "home"),
path('signup/',views.signup, name = "signup"),
path('signin/',views.signin, name = "signin"),
path('resetpassword/',views.resetpassword, name = "resetpassword"),
#path('signout/',views.signout, name = "signout"),


]