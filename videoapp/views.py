from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from videoapp.models import Video


class VideoDetailView(DetailView):
    model = Video
    context_object_name = 'target_video'
    template_name = 'videoapp/video_detail.html'


class VideoListView(ListView):
    model = Video
    context_object_name = 'video_list'
    template_name = 'videoapp/video_list.html'
    paginate_by = 8
