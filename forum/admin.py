from django.contrib import admin
from .models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'date',
        'approved',
        'category',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'user',
        'date',
        'content',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
