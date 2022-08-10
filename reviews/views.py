from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm


class ReviewView(View):
    def get(self, req: HttpRequest):
        form = ReviewForm()
        return render(req, "reviews/review.html", {"form": form})

    def post(self, req: HttpRequest):
        form = ReviewForm(req.POST)

        if form.is_valid():
            form.save()  # save to db
            return HttpResponseRedirect("/thank-you")

        return render(req, "reviews/review.html", {"form": form})


def thank_you(req: HttpRequest) -> HttpResponse:
    return render(req, "reviews/thank_you.html")
