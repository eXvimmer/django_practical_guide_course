from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from .models import Book


def index(request: HttpRequest):
    books = Book.objects.all()  # type: ignore
    return render(request, "book_outlet/index.html", {"books": books})


def book_detail(request: HttpRequest, slug: str):
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "rating": book.rating,
            "title": book.title,
            "author": book.author,
            "is_bestseller": book.is_bestseller,
        },
    )
