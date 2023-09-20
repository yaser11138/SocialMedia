from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
# Create your views here.


@login_required
def add_post(request):
    if request.method == "POST":
        user = request.user
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = user
            post.save()
            return redirect("visit_profile")
        else:
            return render(request, "posts/add-post.html", context={"form": post_form})

    else:
        form = PostForm()
        return render(request, "posts/add-post.html", context={"form": form})


def view_post(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post-detail.html", context={"post": post})
