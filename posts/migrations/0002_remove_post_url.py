# Generated by Django 4.2.4 on 2023-09-16 07:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="url",
        ),
    ]
