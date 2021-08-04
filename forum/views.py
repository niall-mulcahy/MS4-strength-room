from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Author, Post, Category, Comment
from .forms import NewPostForm


# Create your views here.
def forum(request):
    """ This page is designed to show all the posts """

    posts = Post.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posts = posts.filter(category__title__in=categories)
            categories = Category.objects.filter(title__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criterea!")
                return redirect(reverse('posts'))
            queries = Q(title__icontains=query) | Q(content__icontains=query)
            posts = posts.filter(queries)

    context = {
        'posts': posts,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'forum/forum.html', context)


def post_detail(request, post_id):
    """ A view to return all specific data associated with one post """

    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.all()
    author = Author.objects.get(user=request.user)

    if request.method == "POST":
        comment = request.POST.get("comment")
        Comment.objects.get_or_create(
            post=post,
            user=author,
            content=comment,
        )

    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'forum/post_detail.html', context)


def new_post(request):

    posts = Post.objects.all()
    author = Author.objects.get(user=request.user)

    if request.method == "POST":
        title = request.POST.get("title")
        categoryid = request.POST.get("category")
        content = request.POST.get("content")
        Post.objects.get_or_create(
            user=author,
            title=title,
            category_id=categoryid,
            content=content,
        )
        print(author)
        print(content)

        return HttpResponseRedirect(reverse('forum'))

    new_post_form = NewPostForm()
    template = 'forum/new_post.html'
    context = {
        'new_post_form': new_post_form,
        'posts': posts
    }

    return render(request, template, context)
