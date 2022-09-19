from ast import Not
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Posts
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def home(request):
    user = request.user
    if user.is_authenticated:
        post_list = Posts.objects.all().order_by('-pub_date')
        return render(request, "home.html", {"post_list": post_list, "user": user})
    else:
        return redirect('login')

def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        
    return render(request, "login.html")