from django.shortcuts import render, redirect, get_object_or_404, Http404, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login as dj_login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
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
            return render(
                request,
                "Accounts/templates/registration/login.html",
                context={"form": user_form},
            )
    else:
        login_form = AuthenticationForm()
        return render(
            request,
            "Accounts/templates/registration/login.html",
            context={"form": login_form},
        )


def register(request):
    if request.method == "POST":
        user_form = MyUserCreationForm(data=request.POST)
        if user_form.is_valid():
            user_form.cleaned_data["is_active"] = False
            user = user_form.save()
            id = user.id
            endcode_id = encode_int_urlsafe(id)
            secret_code = secert_code_genarator()
            request.session["verify_code"] = secret_code
            send_mail(
                "verify_code",
                f"Hello Here is your verification code {secret_code}",
                "from@example.com",
                [user.email],
            )
            return redirect("verify_secret_code", user_id=endcode_id)
        else:
            return render(
                request, "accounts/register.html", context={"form": user_form}
            )
    else:
        uesr_register_form = MyUserCreationForm()
        return render(
            request, "accounts/register.html", context={"form": uesr_register_form}
        )


@login_required
def update_profile(request):
    if request.method == "POST":
        user_data = MyUserChangeForm(
            instance=request.user, data=request.POST, files=request.FILES
        )
        if user_data.is_valid():
            user_data.save()
            messages.success(request, "Profile updated successfully")
            return redirect(
                reverse("visit_profile", kwargs={"username": request.user.username})
            )
        else:
            return render(
                request, "accounts/update_profile.html", context={"form": user_data}
            )
    else:
        user_form = MyUserChangeForm(instance=request.user)
        return render(
            request, "accounts/update_profile.html", context={"form": user_form}
        )


@login_required
def visit_profile(request, username):
    user = get_object_or_404(klass=User, username=username)
    if user.is_active:
        posts = user.posts.all()
        paginator = Paginator(posts, 9)
        try:
            page_number = request.GET.get("page")
            current_page_posts = paginator.page(page_number)
        except PageNotAnInteger:
            current_page_posts = paginator.page(1)
        except EmptyPage:
            raise Http404("The page Not Found")
        return render(
            request,
            "accounts/profile.html",
            context={"posts": current_page_posts, "user": user},
        )
    raise Http404("The page Not Found")


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
                return redirect("visit_profile", username=user.username)
            else:
                form_errors = {"invalid_code": "Code is Not Correct"}
        else:
            form_errors = code_form.errors

    form = SecertCodeForm()
    return render(
        request,
        "accounts/secret_code.html",
        context={"form": form, "form_errors": form_errors},
    )


@login_required
@require_POST
def follow(request):
    following_user_id = request.POST.get("id")
    following_user = User.objects.get(id=following_user_id)
    follower_user = request.user
    if following_user not in follower_user.following.all():
        follower_user.following.add(following_user)
        return JsonResponse(data={"data": "fuck you"})
    else:
        follower_user.following.remove(following_user)
        return JsonResponse(data={"data": "fuck you more"})
