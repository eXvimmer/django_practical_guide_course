from django.forms import forms


class ProfileForm(forms.Form):
    user_image = forms.FileField()
