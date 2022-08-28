from rest_framework import viewsets
from .models import Message, Topic
from .serializers import MessageSerializer, TopicSerializer
from .permissions import IsOwnerOrReadOnly


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        queryset = Topic.objects.all().select_related(
            'owner',
        )
        return queryset


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        topic_slug = self.kwargs.get('topic_slug')

        queryset = Message.objects.filter(
            topic__slug=topic_slug,
        )
        return queryset
