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
