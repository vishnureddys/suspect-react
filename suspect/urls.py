"""suspect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings #new4
from django.urls import path, include#new
from django.views.generic.base import TemplateView #new2
from django.conf.urls.static import static #new4
from posts import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', accounts_views.register, name = 'register'),
    path('accounts/',include('accounts.urls')), #new3
    path('accounts/',include('django.contrib.auth.urls')), #new
    path('',TemplateView.as_view(template_name='home/home.html'), name = 'home'), #new2
    path('',include('posts.urls')), #new4,
    path('',include('sendemail.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True), name='login'),
    path('',include('suspectnumber.urls')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)