from django.shortcuts import render, Http404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from posts.models import Post


# Create your views here.

@login_required
def homepage(request):
    if request.user.is_authenticated:
        user = request.user
        my_posts = user.posts.all()
        following_post = Post.objects.none()
        for friend in user.following.all():
            following_post = following_post | friend.posts.all()
        all_posts = my_posts | following_post
        paginator = Paginator(all_posts, per_page=3)
        num_pages = paginator.num_pages
        try:
            page_number = request.GET.get("page")
            current_page_posts = paginator.page(page_number)
        except PageNotAnInteger:
            current_page_posts = paginator.page(1)
        except EmptyPage:
            raise Http404("Page Not Found")
        return render(request, "homepage/homepage.html", context={"posts": current_page_posts, "num_pages": num_pages})
    else:
        return None
