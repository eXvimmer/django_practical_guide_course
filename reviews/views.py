from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review


def review(req: HttpRequest):
    if req.method == "POST":
        form = ReviewForm(req.POST)

        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            review_text = form.cleaned_data["review_text"]
            rating = form.cleaned_data["rating"]

            review = Review(user_name=user_name, review_text=review_text, rating=rating)
            review.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    # GET
    return render(req, "reviews/review.html", {"form": form})


def thank_you(req: HttpRequest) -> HttpResponse:
    return render(req, "reviews/thank_you.html")
