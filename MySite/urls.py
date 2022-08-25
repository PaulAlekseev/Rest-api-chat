from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from chat.views import TopicViewSet, MessageViewSet


router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet)
router.register(r'watch/(?P<topic_slug>[\w-]+)', MessageViewSet, basename='messages')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include(router.urls)),
]
