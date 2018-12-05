from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here

def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
                auth.login(request,user)
                return redirect('index')
        else:
                messages.error(request,"wrong data")
                return redirect('login')   

     else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
                if User.objects.filter(username=username).exists():
                       messages.error(request,"uSERNAME Taken")
                       return redirect('register')
                else:
                        user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                        auth.login(request,user)
                        return redirect('index')         
        else:
                messages.error(request,"The password isnt the same")
                return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return True    