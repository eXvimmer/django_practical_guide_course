from django.http import HttpRequest, HttpResponse

# Create your views here.
def january(_: HttpRequest):
    return HttpResponse("Code every day")

def february(_: HttpRequest):
    return HttpResponse("Prepare for a long valentine day")
