from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the dxxcodecoverage Page</h1>")

def detail(request , album_id):
    return HttpResponse("<h2> Details : " + str(album_id))
