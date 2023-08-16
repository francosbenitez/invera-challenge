import pytest
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIClient

User = get_user_model


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.create_user(
        password="holaquetal",
        last_login=timezone.now(),
        is_admin=False,
        email="francosbenitez@gmail.com",
        first_name="Franco",
        is_active=True,
        is_staff=False,
        last_name="Benitez",
        is_email_verified=False,
    )

    EmailAddress.objects.create(
        user=user,
        email=user.email,
        primary=True,
        verified=True,
    )

    return user
