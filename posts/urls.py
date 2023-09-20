from django.urls import path
from .views import add_post, view_post

urlpatterns = [
    path("add/", add_post, name="add_post"),
    path("<slug:slug>/", view_post, name="view_post"),
]