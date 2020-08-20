from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import VideoForm
from .models import Genre, Video


# Create your views here
@csrf_exempt
def index(request):
    if request.method == 'POST':
        return HttpResponse(f'data -- {request.POST}')
    genres = Genre.objects.all()
    video = Video.objects.first()
    myvideoform = VideoForm()
    #return HttpResponse('Welcome to Crappy Netflix')
    return render(request, 'index.html', {'video': video, 'genres': genres, 'myform': myvideoform})