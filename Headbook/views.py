from django.shortcuts import render,redirect

from posts.models import Post

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