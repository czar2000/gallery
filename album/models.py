from django.db import models
from django.utils import timezone
# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=45)
    pic = models.FileField()


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete= models.CASCADE)
    photo_name = models.CharField(max_length=45)
    caption = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    captured = models.DateTimeField(default=timezone.now)
    picture = models.FileField()
