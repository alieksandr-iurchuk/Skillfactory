from django.contrib import admin
from .models import PostCategory, Post

admin.site.register(Post)
admin.site.register(PostCategory)
# Register your models here.
