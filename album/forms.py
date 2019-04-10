from . models import Album, Photo
from django import forms


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_name', 'pic']


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['album', 'photo_name', 'caption', 'location', 'captured', 'picture']
