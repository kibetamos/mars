from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('index1', views.index, name='index1'),
    path('counter', views.counter, name='counter')

]
