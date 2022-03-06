from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.urls.base import reverse

monthly_challenges = {
    "january": "Code every day",
    "february": "Prepare for a long valentine day",
    "march": "Learn basics of hacking just for fun",
    "april": "Learn C++ programming language",
    "may": "Learn Golang",
    "june": "Go to France",
    "july": "Learn 1500 new French words",
    "august": "Get deep into hacking",
    "september": "Celebrate your existence",
    "october": "Master TypeScript",
    "november": "Build a better website for yourself with NextJS",
    "december": "Master Django"
}


months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

def numerical_monthly_challenge(_: HttpRequest, month: int):
    """
    Redirects to monthly_challenge if the number is between 1 and 12, otherwise
    sends a http not found response
    """
    if 1 <= month <= 12:
        redirect_month = months[month - 1]
    else:
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_path = reverse("monthly_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(_: HttpRequest, month: str):
    """Sends the apopriate response for monthly challenges request"""
    try:
        challenge_text = monthly_challenges[month.lower()]
        response_data = "<h1>{challenge_text}</h1>".format(challenge_text=challenge_text)
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
