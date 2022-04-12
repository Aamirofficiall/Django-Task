from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django import forms
from .models import *


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.add_message(request, messages.INFO, 'User registration completed for user "{}" '.format(obj.email))
            return redirect("login")
        else:
            return render(request, "registration/register.html", {"form":form})
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form":form})

def login_view(request):
    logout(request)
    email = password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        form = LoginForm(request.POST)  

        if not CustomUser.objects.filter(email=email).exists():
            form.add_error('email',"Email not found")
            return render(request,'registration/login.html',{'form':form})
        
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.INFO, "Login successful")
                return redirect('home')
            else:
                form.add_error('email',"User is in-active")   
                return render(request,'registration/login.html',{'form':form})
                   
        else:
            form.add_error('password',"Password is incorrect")
            return render(request,'registration/login.html',{'form':form})
            
    form=LoginForm()
    return render(request,'registration/login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Logout Successfully")
    
    return redirect('home')

def home(request):
    context = {}
    role = request.user.role if  request.user.is_authenticated == True else ''
    if request.user.is_superuser == True:
        context['role'] = 'Admin User'
    else:
        context['role'] =role  if role != None else ''
        
    return render(request,'home.html',context)



####################################################
#             Default Error pages                  #
####################################################



def error_404(request, exception):
    return render(request,'404.html')

def error_500(request):
    return render(request,'500.html')
    