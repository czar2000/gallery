from django.urls import path
from . import views

app_name = 'album'

urlpatterns =[
    path('', views.index, name='album_list'),
    path('(?P<album_id>[0-9]+)/', views.pict, name='photo_list'),

]