# Generated by Django 4.2.4 on 2023-11-11 07:44

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0004_alter_myuser_photo"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="myuser",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
