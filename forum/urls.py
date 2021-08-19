from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('new_post/', views.new_post, name='new_post'),
    path('<post_id>/post_detail', views.post_detail, name='post_detail'),
    path('<post_id>/delete_post', views.delete_post, name='delete_post'),
    path('<post_id>/edit_post', views.edit_post, name='edit_post'),
    path('forum_admin/', views.forum_admin, name='forum_admin'),
    path('<post_id>/approve_post/', views.approve_post, name='approve_post'),
]
