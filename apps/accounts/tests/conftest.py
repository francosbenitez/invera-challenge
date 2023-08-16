import pytest
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.test import Client
from django.utils import timezone

User = get_user_model()


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        password="holaquetal",
        last_login=timezone.now(),
        is_admin=False,
        email="francosbenitez@gmail.com",
        first_name="Franco",
        is_active=True,
        is_staff=False,
        last_name="Benitez",
    )


@pytest.fixture
def verified_email(user):
    email = EmailAddress.objects.create(
        user=user,
        email=user.email,
        primary=True,
        verified=True,
    )

    return email
