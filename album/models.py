from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=45)
    pic = models.FileField()

    def get_absolute_url(self):
        return reverse('album:album_list')


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete= models.CASCADE)
    photo_name = models.CharField(max_length=45)
    caption = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    captured = models.DateTimeField(default=timezone.now)
    picture = models.FileField()

    def get_absolute_url(self):
        return reverse('album:photo_list', args=[str(self.pk)])