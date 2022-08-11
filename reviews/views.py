from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

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


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "We received your feedback!"
        return context  # You should return the context
