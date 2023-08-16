import logging

import pytest

logger = logging.getLogger(__name__)


@pytest.mark.django_db
class TestUserAuthentication:
    registration_url = "/api/accounts/registration/"
    login_url = "/api/accounts/login/"

    def test_successful_user_registration(self, client):
        """
        Test successful user registration.
        """
        payload = {
            "first_name": "Franco",
            "last_name": "Benitez",
            "email": "francosbenitez_2@gmail.com",
            "password1": "holaquetal",
            "password2": "holaquetal",
        }

        response = client.post(self.registration_url, payload)
        logger.info(f"Registration Response: {response.data}")

        assert response.status_code == 201

    def test_successful_user_login(self, client, user):
        """
        Test successful user login.
        """
        response = client.post(
            self.login_url, {"email": user.email, "password": "holaquetal"}
        )
        logger.info(f"Login Response: {response.data}")

        assert response.status_code == 200

    def test_failed_login_invalid_credentials(self, client):
        """
        Test failed user login due to invalid credentials.
        """
        payload = {
            "email": "nonexistentuser@email.com",
            "password": "nonexistentuser",
        }

        response = client.post(self.login_url, payload)
        logger.info(f"Failed Login Response: {response.data}")

        assert response.status_code == 400
        assert response.json() == {
            "non_field_errors": ["Unable to log in with provided credentials."]
        }
