from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields = ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender', 'password')

class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta(UserChangeForm):
        model = Account
        fields = ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender', 'is_active', 'is_staff', 'is_superuser')