from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login as dj_login


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
        return render(request, "Accounts/login.html", context={"form": login_form})

