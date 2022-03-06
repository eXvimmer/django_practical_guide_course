from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseNotFound


def monthly_challenge(_: HttpRequest, month: str):
    """Sends the apopriate response for monthly challenges request"""

    challenge_text = ""
    month = month.lower()
    if month == "january":
        challenge_text = "Code every day"
    elif month == "february":
        challenge_text = "Prepare for a long valentine day"
    elif month == "march":
        challenge_text = "Learn basics of hacking just for fun"
    else:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challenge_text)
