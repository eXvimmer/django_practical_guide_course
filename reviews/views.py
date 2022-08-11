from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView

from .models import Review
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


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"  # instead of object_list

    # to narrow down the query (kinda like pagination)
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte=4)
    #     return data


class ReviewDetailView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.get(pk=kwargs["id"])  # type: ignore
        context["review"] = review
        return context
