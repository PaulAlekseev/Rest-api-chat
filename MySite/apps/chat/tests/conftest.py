import pytest
from django.urls import reverse


@pytest.fixture
def topics_url():
    return reverse('chat:topics-list')