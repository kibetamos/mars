from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('home', views.home, name='home'),
    path('counter', views.counter, name='counter'),
    path('instagram', views.instagram, name='instagram'),
    path('youtube', views.youtube, name='youtube'),


]
