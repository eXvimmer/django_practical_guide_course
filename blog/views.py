from django.http import HttpRequest
from django.shortcuts import render


def starting_page(request: HttpRequest):
    return render(request, "blog/index.html")


def posts(request: HttpRequest):
    return render(request, "blog/all-posts.html")


def post_detail(request: HttpRequest, slug):
    return render(request, "blog/post-detail.html")
