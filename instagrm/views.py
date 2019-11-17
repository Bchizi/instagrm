from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, User, UserProfile
from .forms import UserForm, UserProfileForm, CommentForm, PostForm


# Create your views here.
@login_required
def index(request):
    current_user = request.user
    posts = Post.objects.all()
    return render(request, "instagrm/index.html", context={"posts":posts,
                                                           "current_user":current_user})

@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    profile = UserProfile.objects.get(id=id)
    posts = Post.objects.filter(profile__id=id)
    return render(request, "instagrm/profile.html", context={"user":user,
                                                             "profile":profile,
                                                             "posts":posts})

def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponseRedirect(reverse("user_login")) #raise error/ flash

        else:
            pass #raise error/ flash
    else:
        return render(request, "auth/login.html", context={})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

            return HttpResponseRedirect(reverse("user_login"))

        else:
            pass

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, "auth/register.html", context={"user_form":user_form,
                                                          "profile_form":profile_form,
                                                          "registered":registered})
        