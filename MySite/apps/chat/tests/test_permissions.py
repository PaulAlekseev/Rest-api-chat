import pytest


@pytest.mark.django_db
def test_topic_get_method_is_allowed_to_any_user(api_client, topics_url):
    response = api_client.get(topics_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic_post_method_is_allowed_authenticated_user(api_client, topics_url, token):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    post_data = {
        'name': 'bruh',
        'slug': 'bruh'
    }
    response = api_client.post(topics_url, data=post_data)
    assert response.status_code == 201
