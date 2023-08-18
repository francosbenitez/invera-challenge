from logging import getLogger

import pytest

logger = getLogger(__name__)


@pytest.mark.django_db
def test_successful_user_registration(api_client, registration_url, user_data):
    response = api_client.post(registration_url, user_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_successful_user_login(api_client, login_url, valid_user):
    response = api_client.post(
        login_url, {"email": valid_user.email, "password": "holaquetal"}
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_failed_login_invalid_credentials(api_client, login_url, invalid_user):
    response = api_client.post(login_url, invalid_user)
    assert response.status_code == 400
    assert response.json() == {
        "non_field_errors": ["Unable to log in with provided credentials."]
    }
