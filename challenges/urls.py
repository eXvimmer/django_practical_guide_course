from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.numerical_monthly_challenge),
    path("<str:month>", views.monthly_challenge, name="monthly_challenge")
]
