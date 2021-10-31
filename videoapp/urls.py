from django.urls import path

from videoapp.views import VideoListView, VideoDetailView, add_youtube

app_name = "videoapp"

urlpatterns = [
    path('list/', VideoListView.as_view(), name='list'),
    path('detail/<int:pk>', VideoDetailView.as_view(), name='detail'),
    path('youtube/', add_youtube, name='csv업데이트')
]
