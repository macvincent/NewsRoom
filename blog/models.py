# TODO: Add way to verify area of expertice of users and rank comments based on that
from django.db import models
from django import forms
from django.contrib.auth.models import User

def get_image_path(instance, filename):
    if UserProfile.objects.filter(user=instance.user).first() is not None:
        UserProfile.objects.filter(user=instance.user).first().image.delete()
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class NewsRoom(models.Model):
    title = models.TextField(default="Unknown source", null=True)
    post = models.TextField(default="A Comment..", null=True)
    image = models.TextField(default="Image url", null=True)
    url = models.TextField(default="#", null=True)
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

# one to one and form
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=get_image_path, null=True)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']