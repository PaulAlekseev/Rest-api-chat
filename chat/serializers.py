from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from chat.models import Message, Topic


class MessageSerializer(ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_active = serializers.HiddenField(default=True)

    class Meta:
        model = Message
        fields = '__all__'


class TopicSerializer(ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_active = serializers.HiddenField(default=True)

    class Meta:
        model = Topic
        fields = '__all__'
