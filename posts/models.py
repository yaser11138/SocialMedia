from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
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
        return self.title

    def get_absolute_url(self):
        return reverse("view_post", kwargs={"slug": self.slug })

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


