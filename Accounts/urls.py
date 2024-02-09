from django.urls import path
from django.contrib.auth import views as dj_views
from .views import (
    login,
    register,
    update_profile,
    visit_profile,
    verify_secret_code,
    follow,
)

urlpatterns = [
    path("login/", dj_views.LoginView.as_view(), name="login"),
    path("logout/", dj_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("update_profile/", update_profile, name="update_profile"),
    path("profile/<str:username>/", visit_profile, name="visit_profile"),
    path("follow/", follow, name="follow"),
    # password change and reset password urls
    path(
        "password-change/",
        dj_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change-done/",
        dj_views.PasswordChangeView.as_view(),
        name="password_change_done",
    ),
    path(
        "password-reset/", dj_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password-reset-done/",
        dj_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        dj_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-confirm-complete/",
        dj_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("verify_code/<str:user_id>", verify_secret_code, name="verify_secret_code"),
]
