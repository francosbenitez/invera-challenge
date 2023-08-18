import pytest
from rest_framework.test import APIClient

from apps.accounts.tests.factories import UserFactory


@pytest.fixture
def api_client():
    """
    Returns an APIClient instance.
    """

    return APIClient()


@pytest.fixture
def user():
    """
    Returns a sample user.
    """

    return UserFactory()


@pytest.fixture
def authenticated_api_client(api_client, user):
    """
    Returns an authenticated APIClient instance.
    """

    api_client.force_authenticate(user=user)

    return api_client
