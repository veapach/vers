# chat/models.py
from django.db import models
from django.contrib.auth.models import User  # Используем встроенную модель пользователя


# Модель для каналов (чатов)
class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название чата
    description = models.TextField(blank=True)  # Описание чата
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Кто создал чат

    def __str__(self):
        return self.name


# Модель для сообщений
class Message(models.Model):
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="messages"
    )  # К какому чату относится
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Кто отправил сообщение
    content = models.TextField()  # Текст сообщения
    timestamp = models.DateTimeField(auto_now_add=True)  # Время отправки

    def __str__(self):
        return (
            f"{self.user.username}: {self.content[:20]}"  # Первые 20 символов сообщения
        )
