from django.http import HttpRequest
from django.shortcuts import render


def starting_page(request: HttpRequest):
    return render(request, "blog/index.html")


def posts(_: HttpRequest):
    pass


def post_detail(_: HttpRequest):
    pass
