from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    Model = Review
    # fields = "__all__"
    form_class = ReviewForm  # NOTE: you can remove this completely
    template_name = "reviews/review.html"
    success_url = "thank-you"


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


class ReviewDetailView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
