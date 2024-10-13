# chat/serializers.py
from rest_framework import serializers
from .models import Channel, Message


# Сериализатор для чатов
class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


# Сериализатор для сообщений
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
