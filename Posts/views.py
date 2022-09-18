from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Posts
from django.http import HttpResponse

def home(request):
    user = request.user
    if user.is_authenticated:
        post_list = Posts.objects.all().order_by('-pub_date')
        return render(request, "home.html", {"post_list": post_list, "user": user})
    else:
        return HttpResponse("Login First")