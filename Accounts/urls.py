from django.urls import path
from django.contrib.auth import views as dj_views
from .views import login, profile

urlpatterns = [
    path("login/", dj_views.LoginView.as_view(), name="login"),
    path("logout/", dj_views.LogoutView.as_view(), name="logout"),
    path("profile", profile, name="profile"),
    path("password_change/", dj_views.PasswordChangeView.as_view(),name="password-change"),
    path("password-change-done/", dj_views.PasswordChangeView.as_view(), name="password-change-done"),

]