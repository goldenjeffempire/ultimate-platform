from django.urls import re_path
from echoverse_app.consumers import ChatBotConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<session_id>\d+)/$', ChatBotConsumer.as_asgi()),
]
