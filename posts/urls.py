# posts/urls.py
from django.urls import path
from . import views
from .views import ListPost


urlpatterns = [
    path('posts/', views.ListPost.as_view(), name='Post'),
]
