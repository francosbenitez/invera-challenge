import logging

import pytest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my_logger")


@pytest.mark.django_db
def test_register(client):
    """
    Tests that a user can register.
    """

    payload = dict(
        first_name="Franco",
        last_name="Benitez",
        email="francosbenitez_2@gmail.com",
        password1="holaquetal",
        password2="holaquetal",
    )

    response = client.post("/api/accounts/registration/", payload)

    logger.info(f"Response: {response.data}")

    assert response.status_code == 201


@pytest.mark.django_db
def test_login(client, user):
    """
    Tests that a user can login.
    """

    assert user is not None
    assert user.email == "francosbenitez@gmail.com"

    payload = dict(
        email="francosbenitez_2@gmail.com",
        password="holaquetal",
    )

    response = client.post("/api/accounts/login/", payload)

    logger.info(f"Response: {response.data}")

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_fail(client):
    """
    This test should fail because the user does not exist.
    """

    payload = dict(email="nonexistentuser@email.com", password="nonexistentuser")

    response = client.post(
        "/api/accounts/login/",
        payload,
    )

    logger.info(f"Response: {response.data}")

    assert response.status_code == 401
