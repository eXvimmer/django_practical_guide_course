from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from .models import Post


def starting_page(request: HttpRequest):
    # NOTE: Django does not support negative index (when slicing)
    latest_posts = Post.objects.all().order_by("-date")[:3]  # type: ignore
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request: HttpRequest):
    posts_data = Post.objects.all().order_by("-date")  # type: ignore
    return render(request, "blog/all-posts.html", {"all_posts": posts_data})


def post_detail(request: HttpRequest, slug: str):
    post = get_object_or_404(Post, slug=slug)
    return render(
        request, "blog/post-detail.html", {"post": post, "post_tags": post.tags.all()}
    )
