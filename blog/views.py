from django.shortcuts import render
from blog.models import NewsRoom, Comment
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from blog.models import NewsRoom, ProfileForm, UserProfile
from django import forms
from django.urls import reverse_lazy
import requests
import random
from django.contrib.auth.models import User
from django.conf import settings
import os


#A landing page that offers a news feed.
#I mean an actual news feed - not pun intended
#X months later I don't understand this joke
class BlogHome(CreateView):
    model = NewsRoom
    fields = ['title', 'post', 'image']
    news_list = set()
    def get (self, request):
        api_key = "35edd1b6538c47b596c31defeaa68cb6"
        r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey='+api_key).json()
        articles = r['articles']
        self.news_list.clear()
        for i in range(len(articles)):
            image = articles[i]["urlToImage"]
            title = articles[i]["title"]
            post = str(articles[i]["content"])
            post = post.split('[')[0]
            url = articles[i]["url"]
            source = articles[i]["source"]["name"]
            # If image title or post is missing do not include in newsfeed
            if (image is None) or (title is None) or (post == "None") or (url is None):
                continue
            news = NewsRoom(title = title, image = image, post = post, url = url, source = source)
            news.save()
            self.news_list.add(news)
        return render(request, 'static/blog.html', {"news_list": self.news_list})

# Create chat room to discuss about news
class ChatRoom(TemplateView):

    def get (self, request):
        _title = request.GET.get('news')
        _news = NewsRoom.objects.filter(title=_title).first()
        oldComments = Comment.objects.filter(news =_news)
        return render(request, 'static/chatroom.html', {"news": _news ,"comments": oldComments})

    def post(self, request):
        # If User is not authenticated get them to sign up 
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        _title = request.POST.get('title')
        _comment = request.POST.get('newcomment')
        _news = NewsRoom.objects.filter(title=_title).first()

        comment = Comment(comment = _comment, news = _news, name = request.user)
        comment.save()
        oldComments = Comment.objects.filter(news =_news)
        return render(request, 'static/chatroom.html', {"news": _news ,"comments": oldComments})

class ProfileView(TemplateView):
    def get (self, request):
        # If User is not authenticated get them to sign up 
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))      
            
        user = request.user
        # Check who is trying to view the profile
        if request.GET.get('user') is not None:
            username = request.GET.get('user')
            user = User.objects.filter(username = username).first()

        # Get user comments
        comments = Comment.objects.filter(name = user)
        commentsNum = len(comments)

        # Create a dictionary that maps news to comments
        stories = {}
        for comment in comments:
            if comment.news in stories:
                stories[comment.news].append(comment.comment)
            else:
                stories[comment.news] = [comment.comment]
        storiesNum = len(stories)

        image = UserProfile.objects.filter(user=request.user).last()
        # Render dictionary
        return render(request, 'static/profile.html', {"user": user, "storiesNum" : storiesNum, "commentsNum" :  commentsNum, "stories" : stories, 'image' : image})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = UserProfile.objects.filter(user=request.user).first()
            if user is not None:
                user.image = request.FILES['image']
                user.user = request.user
            else:
                user = UserProfile(image=request.POST.get('image'), user=request.user)
            user.save()
        return HttpResponseRedirect(reverse_lazy('profile'))