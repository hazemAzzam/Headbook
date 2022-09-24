from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CustomPostCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Post
        fields = ('account','content')

class CustomPostChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Post
        fields = ('account','content')
