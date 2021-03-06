from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):
    category = models.ForeignKey(
        'Category', default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments",
        default="Bodybuilding", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.content
