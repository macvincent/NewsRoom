from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NewsRoom(models.Model):
    title = models.CharField(max_length = 300)
    post = models.TextField(default="A Comment..", null=True)
    image = models.URLField(default="#", null=True)
    url = models.URLField(default="#")
    source = models.CharField(max_length = 300, null = True)
    
    def __repr__(self):
        return self.title
    def __str__(self):
        return self.title

#Create comment model
class Comment(models.Model):
    news = models.ForeignKey(NewsRoom, on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(default="posts")

