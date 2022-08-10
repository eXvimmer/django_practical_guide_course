from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm


def review(req: HttpRequest):
    if req.method == "POST":
        form = ReviewForm(req.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    # GET
    form = ReviewForm()
    return render(req, "reviews/review.html", {"form": form})


def thank_you(req: HttpRequest) -> HttpResponse:
    return render(req, "reviews/thank_you.html")
