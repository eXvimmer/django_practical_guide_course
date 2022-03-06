from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(_: HttpRequest):
    return HttpResponse("Hello from Django")
