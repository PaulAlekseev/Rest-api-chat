import pytest
from django.urls import reverse


@pytest.fixture
def topics_url():
    return reverse('chat:topics-list')


@pytest.fixture
def new_topic_data():
    data = {
        'name': 'Topic2',
        'slug': 'Topic2'
    }
    return data


@pytest.fixture
def topic_user1(topic_factory, user1):
    return topic_factory.create(owner=user1)


@pytest.fixture
def topic_user1_url(topic_user1):
    return reverse('chat:topics-detail', kwargs={'pk': topic_user1.pk})