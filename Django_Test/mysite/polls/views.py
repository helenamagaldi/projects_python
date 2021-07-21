from django.http import HttpResponse

def index(request):
    return HttpResponse("Haaaaay you're at the polls index")