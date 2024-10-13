# chat/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChannelViewSet, MessageViewSet

router = DefaultRouter()
router.register(r"channels", ChannelViewSet)  # Чаты
router.register(r"messages", MessageViewSet)  # Сообщения

urlpatterns = [
    path("", include(router.urls)),  # Интеграция маршрутов через router
]
