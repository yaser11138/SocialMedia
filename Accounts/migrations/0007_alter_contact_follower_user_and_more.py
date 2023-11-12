# Generated by Django 4.2.4 on 2023-11-11 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0006_contact_myuser_following"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="follower_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact_followers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="following_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact_followings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]