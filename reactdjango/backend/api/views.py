from django.http import HttpResponse

def start(request):
    return HttpResponse('<h1>Hi there</h1>')