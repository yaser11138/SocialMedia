from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login as dj_login
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import MyUserCreationForm, MyUserChangeForm, SecertCodeForm
from .secret import secert_code_genarator, encode_int_urlsafe, decode_int_urlsafe

User = get_user_model()


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
            user = user_form.save()
            id = user.id
            endcode_id = encode_int_urlsafe(id)
            secret_code = secert_code_genarator()
            request.session["verify_code"] = secret_code
            print(secret_code)
            return redirect("verify_secret_code", user_id=endcode_id)
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
    posts = request.user.posts.all()
    return render(request, "accounts/profile.html",context={"posts": posts})


def verify_secret_code(request, user_id):
    form_errors = None

    if request.method == "POST":
        code_form = SecertCodeForm(request.POST)
        if code_form.is_valid():
            secret_code = code_form.cleaned_data.get("secret_code")
            if secret_code == request.session.get("secret_code"):
                id = decode_int_urlsafe(user_id)
                user = User.objects.get(id=id)
                user.is_active = True
                user.save()
                dj_login(request, user)
                return redirect("visit_profile")
            else:
                form_errors = {"invalid_code": "Code is Not Correct"}
        else:
            form_errors = code_form.errors

    form = SecertCodeForm()
    return render(request, "accounts/secret_code.html", context={"form": form, "form_errors": form_errors})

