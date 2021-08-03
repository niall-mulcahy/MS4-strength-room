from django.contrib import admin
from .models import Author, Category, Post, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'fullname',
        'bio',
    )


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
        'user',
        'date',
        'content'
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
