from django.contrib import admin
from .models import Post, Comment


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "slug", "created"]
    list_filter = ["created"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass