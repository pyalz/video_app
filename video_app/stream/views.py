#https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
from django.shortcuts import render,redirect, get_object_or_404
from . models import VidStream

from . forms import VidUploadForm
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from . models import PLAYLIST_CHOICES


#https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/
class GeneralVideoListView(ListView):
    model = VidStream
    template_name = 'stream/video-list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']

def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = VidStream.objects.filter(title__contains=query)
            return render(request, 'stream/search.html',{'videos':results})
    
    return render(request, 'stream/search.html')

def playlist(request):
    if request.method == 'POST':
        query = request.POST.get('playlist', None)
        if query:
            results = VidStream.objects.filter(playlist__contains=query)
            return render(request, 'stream/playlist.html',{'videos':results})
    return render(request, 'stream/playlist.html')


class VideoCreateView(LoginRequiredMixin   ,CreateView):
    model = VidStream    
    login_url = "/admin/login/"    
    success_url = "/"
    template_name = 'stream/post-video.html'
    fields = ['title', 'description', 'playlist','video','author_email']
