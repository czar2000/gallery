from django.urls import path
from . import views

app_name = 'album'

urlpatterns =[
    path('', views.index, name='album_list'),
    path('create_album', views.create_album, name='create_album'),
    path('create_photo', views.create_photo, name='create_photo'),
    path('(?P<album_id>[0-9]+)', views.pict, name='photo_list'),
    path('(?P<album_id>[0-9]+)/delete-album', views.album_delete, name='delete-album'),
    path('<int:pk>/update_album', views.AlbumUpdateView.as_view(), name='update-album'),
]
