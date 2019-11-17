from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment
from pyuploadcare.dj.forms import ImageField

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")


class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = UserProfile
        fields = ("profile_pic", "bio")


class PostForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.Textarea())
    image = ImageField(label='')

    class Meta:
        model = Post
        fields = ("caption", "image")


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Comment
        fields = ("comment")