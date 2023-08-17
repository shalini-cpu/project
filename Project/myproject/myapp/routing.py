from django.urls import re_path
from myapp import consumers

websocket_urlpatterns = [
    re_path(r'ws/$', consumers.MyConsumer.as_asgi()),
]
