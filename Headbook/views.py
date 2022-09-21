from django.shortcuts import render,redirect
from posts.models import Post
from django.contrib.auth import login, logout, authenticate
from accounts.forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
        user = authenticate(request, username=phone_number, password=password)
        print(user.first_name)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"