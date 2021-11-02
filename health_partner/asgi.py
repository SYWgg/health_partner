

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chatapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_partner.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket" : AuthMiddlewareStack(
        URLRouter(
            chatapp.routing.websocket_urlpatterns
        )
    )

})