from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/socket-server/', consumers.ClimateConsumer.as_asgi()),
]