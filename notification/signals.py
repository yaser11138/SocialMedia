from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from posts.models import Comment, Post
from .models import Action


@receiver(post_save, sender=Post)
def new_post_created(sender, instance, created, **kwargs):
    if created:
        Action.objects.create(user=instance.user, action='new_post', content_object=instance)


@receiver(post_save, sender=Comment)
def new_comment_created(sender, instance, created, **kwargs):
    if created:
        Action.objects.create(user=instance.user, action='new_comment', content_object=instance)

