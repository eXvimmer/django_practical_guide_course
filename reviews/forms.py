from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ["user_name", "review_text", "rating"]
        # exclude = ["secret_field"]
        fields = "__all__"
