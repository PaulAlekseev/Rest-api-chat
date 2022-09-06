import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from tests.factories import UserFactory, TokenFactory, TopicFactory, MessageFactory


register(UserFactory)
register(TokenFactory)
register(TopicFactory)
register(MessageFactory)


@pytest.fixture
def user1(db, user_factory):
    return user_factory.create()


@pytest.fixture
def token_user1(db, token_factory, user1):
    return token_factory.create(user=user1)


@pytest.fixture
def user2(db, user_factory):
    return user_factory.create(username='User2', email='User2@mail.com')


@pytest.fixture
def token_user2(db, token_factory, user2):
    return token_factory.create(user=user2)


@pytest.fixture
def api_client():
    return APIClient()
