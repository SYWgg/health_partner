from django.urls import path

from boardapp.views import BoardListView, BoardCreateView, BoardDetailView, BoardUpdateView, BoardDeleteView

app_name = 'boardapp'

urlpatterns = [
    path('list/', BoardListView.as_view(), name='list'),
    path('create/', BoardCreateView.as_view(), name='create'),
    path('detail/<int:pk>', BoardDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BoardUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BoardDeleteView.as_view(), name='delete'),
]