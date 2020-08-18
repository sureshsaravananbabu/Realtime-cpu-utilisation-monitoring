from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from Home import data
from django.urls import path,include

websocket_urlPattern=[
    path('ws/cpu/',data.SendData),
]

application=ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(URLRouter(websocket_urlPattern))   

})