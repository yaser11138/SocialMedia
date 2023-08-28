from django.urls import path
from django.contrib.auth import views as dj_views
from .views import login


urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", dj_views.LogoutView().as_view(), name="logout",)
]