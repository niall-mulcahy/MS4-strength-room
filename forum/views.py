from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Post, Category


# Create your views here.
def forum(request):
    """ This page is designed to show all the posts """

    posts = Post.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            posts = posts.filter(category__in=categories)
            categories = Category.objects.filter(id__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criterea!")
                return redirect(reverse('posts'))
            queries = Q(title__icontains=query) | Q(content__icontains=query)
            posts = posts.filter(queries)

    context = {
        'posts': posts,
        'search_term': query,
    }

    return render(request, 'forum/forum.html', context)


def detail(request, slug):
    """ A view to return all specific data associated with one post """
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }

    return render(request, 'post.html', context)
