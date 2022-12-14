# Generated by Django 4.1.1 on 2022-09-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        default="", max_length=15, verbose_name="First Name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        default="", max_length=15, verbose_name="Last Name"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        default="",
                        max_length=11,
                        unique=True,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        default="2000-01-01", verbose_name="Date of birth"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        default="MALE", max_length=10, verbose_name="Gender"
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(default="media/default.png", upload_to="Media/"),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
