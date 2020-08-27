import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

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
    if os.environ.get('DATABASE_URL'):
        database_url = os.environ.get('DATABASE_URL')
    else:
        database_url = 'Not set'

    context = {
        'videos': videos,
        'genres': genres,
        'myform': myvideoform,
        'database_url': database_url,
    }
    #return HttpResponse('Welcome to Crappy Netflix')
    return render(request, 'netflix/index.html', context)

def search(request):
    if request.method == 'POST':
        return HttpResponse(f'data -- {request.POST}')
    else:
        return HttpResponse('no data posted. Please search first')


class VideoListView(generic.ListView):
    model = Video
    context_object_name = 'videos'

class VideoDetailView(generic.DetailView):
    # TODO: Homework - Add this
    pass