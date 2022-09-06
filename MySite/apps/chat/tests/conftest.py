import pytest
from django.urls import reverse


@pytest.fixture
def topics_url():
    return reverse('chat:topics-list')


@pytest.fixture
def messages_url(topic_user1):
    return reverse('chat:messages-list', kwargs={'topic_slug': topic_user1.slug})


@pytest.fixture
def new_topic_data():
    data = {
        'name': 'Topic2',
        'slug': 'Topic2'
    }
    return data


@pytest.fixture
def new_message_data(topic_user1):
    data = {
        'topic': topic_user1.pk,
        'text': 'Message1'
    }
    return data


@pytest.fixture
def topic_user1(topic_factory, user1):
    return topic_factory.create(owner=user1)


@pytest.fixture
def topic_user1_url(topic_user1):
    return reverse('chat:topics-detail', kwargs={'pk': topic_user1.pk})


@pytest.fixture
def message_user1(message_factory, user1, topic_user1):
    return message_factory.create(owner=user1, topic=topic_user1)


@pytest.fixture
def message_user1_url(topic_user1, message_user1):
    return reverse('chat:messages-detail', kwargs={'topic_slug': topic_user1.slug, 'pk': message_user1.pk})
