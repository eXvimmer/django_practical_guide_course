from django.shortcuts import render
from django.http import HttpRequest

from .models import Book


def index(request: HttpRequest):
    books = Book.objects.all()  # type: ignore
    return render(request, "book_outlet/index.html", {"books": books})
