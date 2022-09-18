from django.db import models
from django.contrib.auth import get_user_model

class Posts(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.author.username
