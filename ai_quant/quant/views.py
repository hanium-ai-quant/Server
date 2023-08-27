from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['nickname'], email=request.POST['email'], password=request.POST['password1'],           
                )
            auth.login(request, user)
            return redirect('quant')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) 
        
        if user is not None:
            auth.login(request, user)
            return redirect('home') 
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'}) 
    else:
        return render(request, 'accounts/login.html')