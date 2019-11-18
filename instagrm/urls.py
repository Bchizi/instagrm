from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^profile/(\d+)", views.profile, name="profile"),
    url(r"^like/(\d+)", views.like, name="like"),
]