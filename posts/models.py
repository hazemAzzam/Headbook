from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Account
# Create your models here.
class Post(models.Model):
    account = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    pub_date=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Post: {self.account} ({self.content})"


class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return f"Comment: {self.account} ({self.comment}) \n ({self.post})"
    

