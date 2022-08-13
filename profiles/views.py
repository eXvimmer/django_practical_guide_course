from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request: HttpRequest):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request: HttpRequest):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            store_file(request.FILES["user_image"])
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {"form": submitted_form})
