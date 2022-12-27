from django.urls import path
from . import views
urlpatterns= [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('LikingPost', views.LikingPost, name='LikingPost'),
    path('profile/<str:pk>', views.profile, name='profile')

 ]