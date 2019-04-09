from django.shortcuts import render,  get_object_or_404
from . models import Album, Photo
# Create your views here.


def index(request):
    albums = Album.objects.all()
    return render(request, 'album/album_list.html', {'albums': albums})


def pict(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'album/photo_list.html', {'album': album})

