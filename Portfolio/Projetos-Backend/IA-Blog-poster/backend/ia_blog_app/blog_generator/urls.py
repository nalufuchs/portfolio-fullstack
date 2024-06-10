from django.urls import path
from . import views

#Criar uma função index em views.py que retornará uma string
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
]