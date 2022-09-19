from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'custom'

class UserAdmin(BaseUserAdmin):
    inlines=(CustomUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)