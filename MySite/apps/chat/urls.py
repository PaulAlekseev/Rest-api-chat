from rest_framework import routers
from django.urls import include, re_path

from MySite.apps.chat.views import TopicViewSet, MessageViewSet


app_name = 'chat'

router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet, basename='topics')
router.register(r'topic/(?P<topic_slug>[\w-]+)', MessageViewSet, basename='messages')


urlpatterns = [
    re_path(r'^chat/', include(router.urls)),
]
