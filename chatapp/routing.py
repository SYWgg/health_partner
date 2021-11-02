from django.urls import re_path

from chatapp import consumers

websocket_urlpatterns = [
    re_path(r'', consumers.ChatConsumer.as_asgi()),
]