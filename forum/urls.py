from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('new_post/', views.new_post, name='new_post'),
    path('<post_id>/', views.post_detail, name='post_detail'),
]
