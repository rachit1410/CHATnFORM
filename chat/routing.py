from django.urls import re_path
from chat import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<group_id>[0-9a-f-]+)/$', consumers.ChatConsumer.as_asgi())
]
