from re import L
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    first_name = models.CharField(max_length=15, verbose_name="First Name", default="")
    last_name = models.CharField(max_length=15, verbose_name="Last Name", default="")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number", default="", blank=False, null=False, unique=True)
    date_of_birth = models.DateField(verbose_name="Date of birth", default="2000-01-01", blank=False, null=False)
    Genders = (("MALE", "Male"), ("FEMALE", "Female"))
    gender = models.CharField(max_length=10, verbose_name="Gender", default="MALE", blank=False, null=False)
    profile_picture = models.ImageField(default=f"default.png")
    objects=AccountManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "date_of_birth", "gender"]

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.phone_number

    def has_perm(self, obj=None):
        return self.is_staff

    def has_module_perms(self, label_name=None):
        return True

