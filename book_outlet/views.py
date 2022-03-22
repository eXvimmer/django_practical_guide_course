from django.shortcuts import render
from django.http import HttpRequest, Http404

from .models import Book


def index(request: HttpRequest):
    books = Book.objects.all()  # type: ignore
    return render(request, "book_outlet/index.html", {"books": books})


def book_detail(request: HttpRequest, id: int):
    try:
        book = Book.objects.get(pk=id)  # type: ignore
    except:
        raise Http404()

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
