from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Your Name",
        max_length=100,
        error_messages={
            "required": "name cannot be empty",
            "max_length": "name should be at most 100 characters long",
        },
    )
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=255
    )
    rating = forms.IntegerField(min_value=1, max_value=5, label="Your Rating")
