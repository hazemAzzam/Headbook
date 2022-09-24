from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Permission, Group

class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, date_of_birth, gender, password=None):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            gender=gender,
        )
        user.set_password(password)
        user.full_name = f"{first_name} {last_name}"
        user.save(using=self._db)

        return user
    
    def create_superuser(self, first_name, last_name, phone_number, date_of_birth, gender, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            gender=gender,
            password=password
        )
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    full_name               = models.CharField(max_length=30, null=True)
    first_name              = models.CharField(max_length=15, verbose_name="First Name", default="")
    last_name               = models.CharField(max_length=15, verbose_name="Last Name", default="")
    phone_number            = models.CharField(max_length=11, verbose_name="Phone Number", default="", blank=False, null=False, unique=True)
    date_of_birth           = models.DateField(verbose_name="Date of birth", default="2000-01-01", blank=False, null=False)
    Genders                 = (("MALE", "Male"), ("FEMALE", "Female"))
    gender                  = models.CharField(max_length=10, verbose_name="Gender", default="MALE", blank=False, null=False)
    profile_picture         = models.ImageField(default=f"default.png")

    objects                 = AccountManager()

    USERNAME_FIELD          = "phone_number"
    REQUIRED_FIELDS         = ["first_name", "last_name", "date_of_birth", "gender"]

    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)

    date_joined             = models.DateTimeField(verbose_name="Date Joined", auto_now=True)
    last_login              = models.DateTimeField(verbose_name="Last Login", auto_now_add=True)

    user_permissions        = models.ManyToManyField(Permission)
    groups                  = models.ManyToManyField(Group)
    
    def __str__(self):
        return f"{self.full_name}"

    def has_perm(self, obj=None):
        return self.is_staff

    def has_module_perms(self, label_name=None):
        return True

    
class Friendship(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+', null=True)
    friend = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    friendship_date = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return f"({self.account}) and ({self.friend})"