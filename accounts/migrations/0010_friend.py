# Generated by Django 4.1.1 on 2022-09-22 10:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_remove_account_email_remove_account_username_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Friend",
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
                ("friend", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
