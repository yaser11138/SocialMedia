from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import PostForm, CommentForm
from .models import Post, Comment
from .functions import slug_generator


# Create your views here.


@login_required
def add_post(request):
    if request.method == "POST":
        user = request.user
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            slug = slug_generator()
            post.user = user
            post.slug = slug
            post.save()
            return redirect("visit_profile")
        else:
            return render(request, "posts/add-post.html", context={"form": post_form})

    else:
        form = PostForm()
        return render(request, "posts/add-post.html", context={"form": form})


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/post-detail.html", context={"post": post})


@require_POST
@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user in post.users_like.all():
        print(f"{post.id} liked by {request.user}")
        post.users_like.remove(request.user)
        return JsonResponse(data={"message": "disliked"})
    else:
        print(f"{post.id} like removed by {request.user}")
        post.users_like.add(request.user)
        return JsonResponse(data={"message": "liked"})


@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_from = CommentForm(data=request.POST)
    print(comment_from)
    if comment_from.is_valid():
        comment = comment_from.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return JsonResponse(data={"message": "succses"})
    else:
        return JsonResponse(data=comment_from.errors)
