from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from .models import Book


def index(request: HttpRequest):
    books = Book.objects.all().order_by("-rating")  # type: ignore
    total_books = books.count()  # type: ignore
    avg_rating = books.aggregate(Avg("rating"))
    return render(
        request,
        "book_outlet/index.html",
        {"books": books, "total_books": total_books, "avg_rating": avg_rating},
    )


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
