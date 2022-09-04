import pytest


@pytest.mark.django_db
def test_topic_get_method_is_allowed_to_any_user(api_client, topics_url):
    response = api_client.get(topics_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic_post_method_is_allowed_authorized_user(api_client, topics_url, token_user1, new_topic_data):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.post(topics_url, data=new_topic_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_topic_post_method_is_not_allowed_not_authorized_user(api_client, topics_url, new_topic_data):
    response = api_client.post(topics_url, data=new_topic_data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_topic_put_allowed_authorized_owner(topic_user1_url, token_user1, api_client, new_topic_data):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.put(topic_user1_url, data=new_topic_data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic_put_not_allowed_authorized_not_owner(topic_user1_url, token_user2, api_client, new_topic_data):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user2}')
    response = api_client.put(topic_user1_url, data=new_topic_data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_topic_put_not_allowed_unauthorized(topic_user1_url, token_user1, api_client, new_topic_data):
    response = api_client.put(topic_user1_url, data=new_topic_data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_topic_delete_allowed_authorized_owner(topic_user1_url, token_user1, api_client):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.delete(topic_user1_url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_topic_delete_not_allowed_authorized_not_owner(topic_user1_url, token_user2, api_client):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user2}')
    response = api_client.delete(topic_user1_url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_topic_delete_not_allowed_unauthorized(topic_user1_url, token_user2, api_client):
    response = api_client.delete(topic_user1_url)
    assert response.status_code == 401


