from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
