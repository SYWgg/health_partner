from django.urls import path

from chatapp.views import main_view

app_name = 'chatapp'

urlpatterns = [
    path('', main_view, name='main_view'),
]