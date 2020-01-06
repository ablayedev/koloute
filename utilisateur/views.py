from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('pass')
        print(username+password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard:rapport')
        else:
            print('no')
    return render(request,'utilisateur/index.html')

def admin(request):
    return render(request,'utilisateur/admin.html')

def deconect(request):
    logout(request)
    return redirect('utilisateur:home')