import pytest


@pytest.mark.django_db
def test_topic_get_method_is_allowed_to_any_user(api_client, topics_url):
    response = api_client.get(topics_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic_post_method_is_allowed_authorized_user(api_client, topics_url, token, topics_data):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    response = api_client.post(topics_url, data=topics_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_topic_post_method_is_not_allowed_not_authorized_user(api_client, topics_url, topics_data):
    response = api_client.post(topics_url, data=topics_data)
    assert response.status_code == 401
