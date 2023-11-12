from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="post_likes", blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]

    ordering = ['-created']

    def __str__(self):
        return f"{self.user}=>{self.slug}"

    def get_absolute_url(self):
        return reverse("view_post", args=(self.slug,))

    @property
    def is_updated(self):
        if self.date_updated != self.date_created:
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="comment_likes", blank=True)

    def __str__(self):
        return f"{self.post} {self.user}"
