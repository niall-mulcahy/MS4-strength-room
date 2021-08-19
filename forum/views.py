from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import NewPostForm, AdminPostForm
from profiles.models import UserProfile


from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.core.paginator import Paginator, EmptyPage

User = get_user_model()


@login_required
# Create your views here.
def forum(request):
    """ This page is designed to show all the posts """

    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile.is_member)

    if profile.is_member:
        posts = Post.objects.all().filter(approved=True).order_by('-date')

        p = Paginator(posts, 3)

        page_num = request.GET.get('page', 1)

        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        query = None
        category = None

        if request.GET:
            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                page = posts.filter(category__title__in=categories)
                category = Category.objects.filter(title__in=categories)

            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(
                        request, "You didn't enter any search criterea!")
                    return redirect(reverse('forum'))
                queries = Q(title__icontains=query) | Q(content__icontains=query)
                page = posts.filter(queries)

        context = {
            'posts': posts,
            'page': page,
            'search_term': query,
            'current_categories': category,
        }
        return render(request, 'forum/forum.html', context)

    else:
        messages.error(
            request,
            "You must purchase membership to access this part of the site"
        )
        return redirect(reverse('products'))


def post_detail(request, post_id):
    """ A view to return all specific data associated with one post """

    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.all()
    user = request.user

    if request.method == "POST":
        comment = request.POST.get("comment")
        Comment.objects.get_or_create(
            post=post,
            user=user,
            content=comment,
        )
        messages.info(request, 'Thank you for your comment')

    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'forum/post_detail.html', context)


def new_post(request):

    posts = Post.objects.all()
    user = request.user

    if request.method == "POST":
        title = request.POST.get("title")
        categoryid = request.POST.get("category")
        content = request.POST.get("content")
        Post.objects.get_or_create(
            user=user,
            title=title,
            category_id=categoryid,
            content=content,
        )
        messages.info(request, 'Your post will be added when an admin approves it!')
        return HttpResponseRedirect(reverse('forum'))

    new_post_form = NewPostForm()
    template = 'forum/new_post.html'
    context = {
        'new_post_form': new_post_form,
        'posts': posts
    }

    return render(request, template, context)


def delete_post(request, post_id):
    template = 'forum/delete_post.html'
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        messages.info(request, 'This post has been deleted')
        return HttpResponseRedirect(reverse('forum'))

    context = {
        'post': post
    }

    return render(request, template, context)


def edit_post(request, post_id):
    template = 'forum/edit_post.html'
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    edit_post_form = NewPostForm(
        initial={
            "title": post.title,
            "category": post.category,
            "content": post.content
        }
    )

    if request.method == "POST":
        title = request.POST.get("title")
        categoryid = request.POST.get("category")
        content = request.POST.get("content")
        Post.objects.get_or_create(
            user=user,
            title=title,
            category_id=categoryid,
            content=content,
        )
        messages.info(request, 'Thank you for updating this post')
        return HttpResponseRedirect(reverse('forum'))

    context = {
        'edit_post_form': edit_post_form,
        'post': post,
    }

    return render(request, template, context)


def forum_admin(request):
    template = 'forum/forum_admin.html'

    posts = Post.objects.all().filter(approved=False).order_by('-date')

    admin_post_form = AdminPostForm()

    context = {
        'admin_post_form': admin_post_form,
        'posts': posts,
    }

    return render(request, template, context)


def approve_post(request, post_id):
    if request.user.is_superuser:
        template = 'forum/approve_post.html'

        post = get_object_or_404(Post, pk=post_id)

        admin_post_form = AdminPostForm(
            initial={
                "title": post.title,
                "category": post.category,
                "content": post.content,
                "approved": post.approved,
            }
        )

        if request.method == "POST":
            title = request.POST.get("title")
            categoryid = request.POST.get("category")
            content = request.POST.get("content")
            approved = request.POST.get("approved")
            if approved:
                approved = True
                Post.objects.get_or_create(
                    user=post.user,
                    title=title,
                    category_id=categoryid,
                    content=content,
                    approved=approved,
                )
                # The delete post here refers to the unapproved post object
                post.delete()
                messages.success(request, 'You have approved this post')
                return HttpResponseRedirect(reverse('forum_admin'))
            else:
                approved = False
                Post.objects.get_or_create(
                    title=title,
                    category_id=categoryid,
                    content=content,
                    approved=approved,
                )
                messages.error(request, 'You have rejected this post')
                return HttpResponseRedirect(reverse('forum_admin'))

        context = {
            'admin_post_form': admin_post_form,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Whoops! Looks like you are not logged in as the admin user!')
        return redirect(reverse('home'))
