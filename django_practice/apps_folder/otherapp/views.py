from django.http import HttpResponse


def say_hi(request):
    return HttpResponse("hy")
