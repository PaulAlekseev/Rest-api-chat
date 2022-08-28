from rest_framework import viewsets
from .models import Message, Topic
from .serializers import MessageSerializer, TopicSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination.pagination import MessagePagination, TopicPagination


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    pagination_class = TopicPagination

    def get_queryset(self):
        queryset = Topic.objects.all().select_related(
            'owner',
        )
        return queryset


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    pagination_class = MessagePagination

    def get_queryset(self):
        topic_slug = self.kwargs.get('topic_slug')

        queryset = Message.objects.filter(
            topic__slug=topic_slug,
        )
        return queryset
