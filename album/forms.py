from . models import Album, Photo
from django import forms
from django.contrib.auth.models import User


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_name', 'pic']


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['photo_name', 'caption', 'location', 'captured', 'picture']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
