from rest_framework import viewsets
from .models import Message, Topic
from .serializers import MessageSerializer, TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().select_related(
        'owner',
    )
    serializer_class = TopicSerializer
