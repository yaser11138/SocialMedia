# Generated by Django 4.2.4 on 2023-09-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Accounts", "0002_myuser_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="myuser",
            name="is_active",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
            ),
        ),
    ]
