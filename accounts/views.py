from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm
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


def home(request):
    context = {}
    role = request.user.role if  request.user.is_authenticated == True else ''
    context['role'] =role  if role != None else ''
    return render(request,'home.html',context)



####################################################
#             Default Error pages                  #
####################################################



def error_404(request, exception):
    return render(request,'404.html')

def error_500(request):
    return render(request,'500.html')
    