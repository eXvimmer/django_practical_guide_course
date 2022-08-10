from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ["user_name", "review_text", "rating"]
        # exclude = ["secret_field"]
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "required": "name cannot be empty",
                "max_length": "please enter a shorter name",
            }
        }
