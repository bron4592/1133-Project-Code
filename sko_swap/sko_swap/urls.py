"""sko_swap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from sko import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.register, name='sko/home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='sko/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='sko/logout.html'), name='logout'),
    path('home/', views.home, name='sko/home'),
    path('newPost/', views.createPost, name='sko/newPost'),
    path('account/', views.account, name='sko/account'),
    path('post/<id>/delete/', views.post_delete, name='post-delete'),
]