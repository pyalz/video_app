from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#https://www.educba.com/django-reverse/
#from django.urls import reverse
PLAYLIST_CHOICES = (
    ('playlist1','PLAYLIST1'),
    ('playlist2','PLAYLIST2'),
    ('playlist3','PLAYLIST3'),
    ('playlist4','PLAYLIST4'),
    ('playlist5','PLAYLIST5'),
)


class VidStream(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    playlist = models.TextField(max_length=30,choices=PLAYLIST_CHOICES, default='playlist1' )
    upload_date = models.DateField(default=timezone.now)
    video = models.FileField(upload_to='')
    author_email = models.EmailField(max_length=30,blank=True)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("video-detail", kwargs={"pk":self.pk})
