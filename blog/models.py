# TODO: Add way to verify area of expertice of users and rank comments based on that
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NewsRoom(models.Model):
    title = models.TextField(default="Unknown source", null=True)
    post = models.TextField(default="A Comment..", null=True)
    image = models.URLField(default="#", null=True)
    url = models.URLField(default="#")
    source = models.TextField(default="Unknown source", null=True)
    
    def __repr__(self):
        return self.title
    def __str__(self):
        return self.title

#Create comment model
class Comment(models.Model):
    news = models.ForeignKey(NewsRoom, on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(default="posts")

