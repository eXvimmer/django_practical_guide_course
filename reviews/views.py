from django.http import HttpRequest
from django.shortcuts import render


def review(request: HttpRequest):
    return render(request, "reviews/review.html")
