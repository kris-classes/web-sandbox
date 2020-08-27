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
    videos = Video.objects.all()
    myvideoform = VideoForm()
    context = {
        'videos': videos,
        'genres': genres,
        'myform': myvideoform,
    }
    #return HttpResponse('Welcome to Crappy Netflix')
    return render(request, 'netflix/index.html', context)

def search(request):
    if request.method == 'POST':
        return HttpResponse(f'data -- {request.POST}')
    else:
        return HttpResponse('no data posted. Please search first')
