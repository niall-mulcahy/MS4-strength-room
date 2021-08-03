from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    bio = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.fullname


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


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.content


class Post(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=400)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    comments = models.ManyToManyField(Comment, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
