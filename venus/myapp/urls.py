from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register', views.register, name="register"),

    path('home', views.home, name='home'),
    path('counter', views.counter, name='counter'),


]
