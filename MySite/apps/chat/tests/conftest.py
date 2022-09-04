import pytest
from django.urls import reverse


@pytest.fixture
def topics_url():
    return reverse('chat:topics-list')


@pytest.fixture
def topics_data():
    data = {
        'name': 'some-name',
        'slug': 'some-slug'
    }
    return data
