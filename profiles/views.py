from django.shortcuts import render
from .models import UserProfile


def profile(request, ):
    """Display user profile"""
    template = 'profiles/profile.html'
    user_data = UserProfile.objects.all()
    context = {
        'user_data': user_data
    }

    return render(request, template, context)
