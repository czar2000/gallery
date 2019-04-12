from django.shortcuts import render,  get_object_or_404, redirect
from . models import Album, Photo
from django.views.generic import CreateView, UpdateView, ListView
from .forms import AlbumForm, PhotoForm
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='album:login')

def index(request):
    albums = Album.objects.all()
    return render(request, 'album/album_list.html', {'albums': albums})


def pict(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'album/photo_list.html', {'album': album})


def create_album(request):
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.pic = request.FILES['pic']
        album.user = request.user
        album.save()
        return render(request, 'album/album_list.html', {'album': album})
    return render(request, 'album/create_album.html', {'form': form})


def create_photo(request, album_id):
    form = PhotoForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.album = album
        photo.picture = request.FILES['picture']
        photo.save()
        return render(request, 'album/photo_list.html', {'photo': photo})
    return render(request, 'album/create_photo.html', {'form': form})


def album_delete(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    return redirect('/')


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo_name', 'caption', 'location', 'captured', 'picture']
    template_name = 'album/create_photo.html'


def delete_photo(request, album_id, photo_id):
    album = get_object_or_404(Album, pk=album_id)
    photo = get_object_or_404(Photo, pk=photo_id)
    photo.delete()

    return render(request, 'album/photo_list.html', {'album': album})


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['album_name', 'pic']

    template_name = 'album/create_album.html'


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('album:album_list')

    return render(request, 'album/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('album:album_list')

    return render(request, 'registration/login.html')



