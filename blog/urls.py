"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path
import blog.views as views

urlpatterns = [
    path('', views.BlogHome.as_view(), name = 'home'),
    path('chatroom/', login_required(views.ChatRoom.as_view()), name = 'chatroom'),
    path('chatroom/', login_required(views.ChatRoom.as_view()), name = 'viewcomment'),
    path('profile/', login_required(views.ProfileView.as_view()), name = 'profile'),
    path('latest/', views.TrendingStories.as_view(), name = 'trending'),
    path('update/', views.AsyncStories.as_view(), name = 'update_stories'),
]
