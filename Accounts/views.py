from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login as dj_login
from django.contrib import messages
from .forms import MyUserCreationForm, MyUserChangeForm


def login(request):
    if request.method == "POST":
        user_form = AuthenticationForm(request=request, data=request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            dj_login(request, user)
            return redirect("visit_profile")
        else:
            print(1)
            return render(request, "Accounts/templates/registration/login.html", context={"form": user_form})
    else:
        login_form = AuthenticationForm()
        return render(request, "Accounts/templates/registration/login.html", context={"form": login_form})


def register(request):
    if request.method == "POST":
        user_form = MyUserCreationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("visit_profile")
        else:
            return render(request, "accounts/register.html", context={"form": user_form})
    else:
        uesr_register_form = MyUserCreationForm()
        return render(request, "accounts/register.html", context={"form": uesr_register_form})


@login_required
def update_profile(request):
    if request.method == "POST":
        user_data = MyUserChangeForm(instance=request.user, data=request.POST, files=request.FILES)
        if user_data.is_valid():
            user_data.save()
            messages.success(request, "Profile updated successfully")
            return redirect("visit_profile")
        else:
            return render(request, "accounts/update_profile.html", context={"form": user_data})
    else:
        user_form = MyUserChangeForm(instance=request.user)
        return render(request, "accounts/update_profile.html", context={"form": user_form})


@login_required
def visit_profile(request):
    return render(request, "accounts/profile.html")
