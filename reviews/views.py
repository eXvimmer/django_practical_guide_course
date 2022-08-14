from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView, View

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = str(loaded_review.id) == favorite_id
        return context


class AddFavoriteView(View):
    def post(self, request: HttpRequest):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id  # type: ignore
        # TODO: use the reverse function below
        return HttpResponseRedirect("/reviews/" + review_id)  # type: ignore
