from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login as dj_login
from .forms import MyUserCreationForm, MyUserChangeForm

def login(request):
    if request.method == "POST":
        user_form = AuthenticationForm(request=request, data=request.POST)
        print(user_form.is_valid())
        print(user_form)
        if user_form.is_valid():
            user = user_form.get_user()
            dj_login(request, user)
            return HttpResponse("Well done budy")
        return HttpResponse(user_form.errors)
    else:
        login_form = AuthenticationForm()
        return render(request, "Accounts/templates/registration/login.html", context={"form": login_form})


@login_required
def profile(request):
    return render(request, "registration/profile.html")


def register(request):
    if request.method == "POST":
        user_form = MyUserCreationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse("Well done body")
        else:
            print(user_form.errors)
            return HttpResponse(user_form.errors)
    else:
        uesr_register_form = MyUserCreationForm()
        return render(request, "accounts/register.html", context={"form": uesr_register_form})


def update_profile(request):
    if request.method == "POST":
        user_data = MyUserChangeForm(instance=request.user, data=request.POST, files=request.FILES)
        if user_data.is_valid():
            user_data.save()
            return render(request, "accounts/update_profile.html")
        else:
            print(user_data.errors)
            return HttpResponse("SOMETHING HAPPEND")
    else:
        user_form = MyUserChangeForm(instance=request.user)
        return render(request, "accounts/update_profile.html",context={"form": user_form})


def home(request):
    return render(request, "index.html")