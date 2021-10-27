from django.urls import path

from videoapp.views import VideoListView, VideoDetailView

app_name = "videoapp"

urlpatterns = [
    path('list/', VideoListView.as_view(), name='list'),
    path('detail/', VideoDetailView.as_view(), name='detail'),
]
