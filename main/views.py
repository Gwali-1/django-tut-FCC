from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import User,Profile
@login_required
def index(request):
    return render(request,"main/index.html")


def signup(request):
    if request.method == "POST":
        #get data sent
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")

        if password != confirm_password:
            messages.info(request, "passwords dont match")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.info(request, "user with email already exits")
            return redirect("signup")
        if User.objects.filter(username=username).exists():
            messages.info(request, "username taken, try another")
            return redirect("signup")
        try:
            new_user = User.objects.create_user(username=username,email=email,password=password)
            new_user.save()

            #log user in and redirect to setting page 
            user = authenticate(request,username=username,password=password)
            login(request,user)
            
            #give user a profile
            user_model = User.objects.get(username=username)
            # new_profile = Profile.objects.create(user=request.user, id_user=request.user.id)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            messages.info(request, "account created succesfully")

            return redirect("settings")
        except Exception as e:
            
            messages.info(request, "something went wrong")
            return redirect("signup")

    print('get')
    return render(request, "main/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            return redirect("index")
        messages.info(request,"invalid credentials")
        return redirect("signin")
    return render(request, "main/signin.html")

def log_out(request):
    logout(request)
    return redirect("signin")


@login_required
def settings(request):
    return render(request, "main/setting.html")