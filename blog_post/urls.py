from django.urls import path
from .views import *


urlpatterns = [
	path('blog-list/', blog_list, name='blog-list'),
	path('blog-single/<str:pk>', blog_single, name='blog-single'),
	path('tag/<slug:tag_slug>/', posts_with_tag, name='post_list_by_tag'),
    path('like/<int:pk>/', like_blog, name='like_blog'),
]