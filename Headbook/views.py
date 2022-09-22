from django.shortcuts import render,redirect
from posts.models import Post
from django.contrib.auth import login, logout, authenticate
from accounts.forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import RegistrationForm

def home(request):
    user = request.user
    if user.is_authenticated:
        post_list = Post.objects.all().order_by('-pub_date')
        return render(request, "home.html", {"post_list": post_list, "user": user})
    return render(request, "login.html")

def add_post(request):
    if request.method == "POST" and request.user.is_authenticated:
        author = request.user
        content = request.POST['new-post-content']
        Post(author=author, content=content).save()
    return redirect('home')
    
def delete_post(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        print(post)
        if request.user == post.author:
            print("Deleted")
            post.delete()


    return redirect('home')

def login_user(request):
    if request.method == 'POST':
        phone_number=request.POST["phone_number"]
        password=request.POST["password"]
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone_number = request.POST["phone_number"]
        password = request.POST["password"]
        gender = 'male'
        try:
            gender = request.POST["female"]
            gender = 'Female'
        except:
            gender = 'Male'
        
        user = Account.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
            date_of_birth='2000-01-01',
            gender=gender,
        )
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html')
