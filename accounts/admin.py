from re import search
from socket import fromshare
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django import forms
from .forms import *


class AccountAdmin(UserAdmin):
    fieldsets= (
        (None, {"fields": ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender', 'profile_picture', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide", ),
                "fields": ("first_name", "last_name" ,"phone_number", "password1", "password2", "date_of_birth", "gender", "profile_picture"),
            },
        ),
    )

    #form=CustomUserChangeForm
    #add_form=CustomUserCreationForm

    list_display = ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender')
    list_filter = ('is_staff', 'is_superuser')
    search_fields=('phone_number',)
    ordering = ('phone_number',)
    filter_horizontal = ()
    
admin.site.register(Account, AccountAdmin)
admin.site.register(Friendship)
admin.site.unregister(Group)
