from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Video


# Create your views here.
def index(request):
    genres = Genre.objects.all()
    video = Video.objects.first()

    #return HttpResponse('Welcome to Crappy Netflix')
    return render(request, 'index.html', {'video': video, 'genres': genres})