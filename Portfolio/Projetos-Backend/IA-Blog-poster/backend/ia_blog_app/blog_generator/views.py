from django.shortcuts import render

# Create your views here.

#Criar uma função index em views.py que requisita um request e retorna um render
def index(request):
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'login.html')

def user_signup(request):
    return render(request, 'signup.html')

def user_logout(request):
    pass