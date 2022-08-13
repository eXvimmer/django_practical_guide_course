from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request: HttpRequest):
        return render(request, "profiles/create_profile.html")

    def post(self, request: HttpRequest):
        store_file(request.FILES["image"])
        return HttpResponseRedirect("/profiles")
