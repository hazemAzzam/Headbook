# Generated by Django 4.1.1 on 2022-09-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_account_is_superuser_alter_account_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="profile_picture",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
    ]