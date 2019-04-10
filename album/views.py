from django.shortcuts import render,  get_object_or_404, redirect
from . models import Album, Photo
from django.views.generic import CreateView, UpdateView
from .forms import AlbumForm, PhotoForm

# Create your views here.


def index(request):
    albums = Album.objects.all()
    return render(request, 'album/album_list.html', {'albums': albums})


def pict(request, album_id):
    photo = get_object_or_404(Photo, pk=album_id)
    return render(request, 'album/photo_list.html', {'photo': photo})


def create_album(request):
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.pic = request.FILES['pic']
        album.user = request.user
        album.save()
        return render(request, 'album/album_list.html', {'album': album})
    return render(request, 'album/create_album.html', {'form': form})


def create_photo(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.picture = request.FILES['picture']
        photo.user = request.user
        photo.save()
        return render(request, 'album/photo_list.html', {'photo': photo})
    return render(request, 'album/create_photo.html', {'form': form})

def album_delete(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    return redirect('/')


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['album_name', 'pic']

    template_name = 'album/create_album.html'
