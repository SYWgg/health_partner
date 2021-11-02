from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView
from trainercommentapp.views import TrainerCommentCreateView, TrainerCommentDeleteView

app_name = 'trainercommentapp'

urlpatterns = [
    path('create/', TrainerCommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', TrainerCommentDeleteView.as_view(), name='delete'),
]