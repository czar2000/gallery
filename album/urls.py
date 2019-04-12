from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'album'

urlpatterns =[
    path('login', views.signin, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.signup, name='signup'),
    path('', views.index, name='album_list'),
    path('create_album', views.create_album, name='create_album'),
    path('(?P<album_id>[0-9]+)/create_photo', views.create_photo, name='create_photo'),
    path('(?P<album_id>[0-9]+)', views.pict, name='photo_list'),
    path('(?P<album_id>[0-9]+)/delete-album', views.album_delete, name='delete-album'),
    path('<int:pk>/update_album', views.AlbumUpdateView.as_view(), name='update-album'),
    path('(?P<album_id>[0-9]+)/delete_photo/(?P<photo_id>[0-9]+)/', views.delete_photo, name='delete_photo'),
    path('<int:pk>/update_photo', views.PhotoUpdateView.as_view(), name='update_photo'),
]
