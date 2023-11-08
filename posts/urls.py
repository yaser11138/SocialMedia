from django.urls import path
from .views import add_post, view_post, like_post, add_comment

urlpatterns = [
    path("add/", add_post, name="add_post"),
    path("<slug:slug>/", view_post, name="view_post"),
    path("like/<int:id>/", like_post, name="like_post"),
    path("comment/add/<int:post_id>/", add_comment, name="add_comment"),
]