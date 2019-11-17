from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "instagrm/index.html", context={"posts":posts})

def profile(request):
    return render(request, "instagrm/profile.html", context={})

def user_login(request):
    pass

def user_logout(request):
    pass

def register(request):
    pass