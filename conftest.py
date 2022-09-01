import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from tests.factories import UserFactory, TokenFactory


register(UserFactory)
register(TokenFactory)


@pytest.fixture
def user(db, user_factory):
    return user_factory.create()


@pytest.fixture
def token(db, token_factory):
    return token_factory.create()


@pytest.fixture
def api_client():
    return APIClient()
