# Generated by Django 4.1.1 on 2022-09-22 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0002_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="content",
            new_name="comment",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="author",
            new_name="account",
        ),
        migrations.AddField(
            model_name="comment",
            name="account",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
