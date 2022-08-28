from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from MySite.apps.chat.views import TopicViewSet, MessageViewSet


router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet, basename='topics')
router.register(r'topic/(?P<topic_slug>[\w-]+)', MessageViewSet, basename='messages')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
