from django.urls import path
from . import views

# app_name = "reviews"

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:id>", views.ReviewDetailView.as_view()),
]
