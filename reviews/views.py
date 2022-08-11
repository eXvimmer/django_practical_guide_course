from django.views.generic import DetailView, FormView, ListView, TemplateView

from .models import Review
from .forms import ReviewForm


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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
