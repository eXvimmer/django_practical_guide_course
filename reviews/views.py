from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def review(request: HttpRequest):
    if request.method == "POST":
        name = request.POST["name"]
        if not name:
            return render(request, "reviews/review.html", {"has_error": True})

        print(name)
        return HttpResponseRedirect("/thank-you")
    # GET
    return render(request, "reviews/review.html", {"has_error": False})


def thank_you(req: HttpRequest) -> HttpResponse:
    return render(req, "reviews/thank_you.html")
