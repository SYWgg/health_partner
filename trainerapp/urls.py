from django.urls import path

from trainerapp import views
from trainerapp.views import TrainerListView, TrainerCreateView, TrainerDetailView, TrainerUpdateView, \
    TrainerDeleteView, InquiredBoardView

app_name = "trainerapp"

urlpatterns = [
    path('list/', TrainerListView.as_view(), name='list'),
    path('create/', TrainerCreateView.as_view(), name='create'),
    path('detail/<int:pk>', TrainerDetailView.as_view(), name='detail'),
    path('update/<int:pk>', TrainerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TrainerDeleteView.as_view(), name='delete'),
    path('board/<int:pk>', InquiredBoardView.as_view(), name='board'),
]
