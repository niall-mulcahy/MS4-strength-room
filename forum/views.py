from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def forum(request):
    """ This page is designed to show all the posts """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'forum/forum.html', context)


def detail(request, slug):
    """ A view to return all specific data associated with one post """
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }

    return render(request, 'post.html', context)
