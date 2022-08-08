from django.http import HttpRequest
from django.shortcuts import render
from .models import Post

posts_data = []


def get_date(post):
    return post["date"]


def starting_page(request: HttpRequest):
    # NOTE: Django does not support negative index (when slicing)
    latest_posts = Post.objects.all().order_by("-date")[:3]  # type: ignore
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request: HttpRequest):
    return render(request, "blog/all-posts.html", {"all_posts": posts_data})


def post_detail(request: HttpRequest, slug: str):
    post = next(post for post in posts_data if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": post})
