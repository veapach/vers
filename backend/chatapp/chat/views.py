# chat/views.py
from rest_framework import viewsets
from .models import Channel, Message
from .serializers import ChannelSerializer, MessageSerializer


# ViewSet для чатов
class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


# ViewSet для сообщений
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
