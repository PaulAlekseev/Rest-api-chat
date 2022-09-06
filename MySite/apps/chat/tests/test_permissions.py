import pytest


@pytest.mark.django_db
def test_topic_get_allowed_to_any_user(api_client, topics_url):
    response = api_client.get(topics_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic_post_allowed_authorized_user(api_client, topics_url, token_user1, new_topic_data):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.post(topics_url, data=new_topic_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_topic_post_not_allowed_not_authorized_user(api_client, topics_url, new_topic_data):
    response = api_client.post(topics_url, data=new_topic_data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_topic_get_allowed_authorized_owner(api_client, topic_user1_url, token_user1):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.get(topic_user1_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic_get_not_allowed_authorized_not_owner(api_client, topic_user1_url, token_user2):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user2}')
    response = api_client.get(topic_user1_url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_topic_get_not_allowed_not_authorized(api_client, topic_user1_url, token_user2):
    response = api_client.get(topic_user1_url)
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


@pytest.mark.django_db
def test_messages_get_allowed_to_any_user(api_client, messages_url, topic_user1):
    response = api_client.get(messages_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_messages_post_allowed_authorized(api_client, messages_url, token_user1, new_message_data):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.post(messages_url, data=new_message_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_messages_post_not_allowed_not_authorized(api_client, messages_url, token_user1, new_message_data):
    response = api_client.post(messages_url, data=new_message_data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_message_get_allowed_authorized_owner(api_client, message_user1_url, token_user1):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.get(message_user1_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_message_get_not_allowed_authorized_not_owner(api_client, message_user1_url, token_user2):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user2}')
    response = api_client.get(message_user1_url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_message_get_not_allowed_not_authorized(api_client, message_user1_url):
    response = api_client.get(message_user1_url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_message_put_allowed_authorized_owner(api_client, message_user1_url, token_user1, new_message_data):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.put(message_user1_url, data=new_message_data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_message_put_not_allowed_authorized_not_owner(api_client, message_user1_url, token_user2, new_message_data):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user2}')
    response = api_client.put(message_user1_url, data=new_message_data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_message_put_not_allowed_not_authorized(api_client, message_user1_url, new_message_data):
    response = api_client.put(message_user1_url, data=new_message_data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_message_delete_allowed_authorized_owner(api_client, message_user1_url, token_user1):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user1}')
    response = api_client.delete(message_user1_url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_message_delete_not_allowed_authorized_not_owner(api_client, message_user1_url, token_user2):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token_user2}')
    response = api_client.put(message_user1_url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_message_delete_not_allowed_not_authorized(api_client, message_user1_url):
    response = api_client.put(message_user1_url)
    assert response.status_code == 401
