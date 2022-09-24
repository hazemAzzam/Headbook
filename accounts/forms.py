from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields = ('full_name','first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender', 'password')

class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta(UserChangeForm):
        model = Account
        #fields=('first_name','last_name',)
        fields = ('full_name','first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender', 'is_active', 'is_staff', 'is_superuser')


class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=11)

    class Meta:
        model = Account
        fields=('first_name', 'last_name', 'phone_number', 'password', 'date_of_birth', 'gender')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            Account.objects.get(phone_number=phone_number)
            print("hi")
        except Exception as e:
            return phone_number
            
        raise forms.ValidationError(f"Phone_number is already in use")

    