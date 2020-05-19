from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import ListView

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''
class PostsPageView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/posts.html'
'''
