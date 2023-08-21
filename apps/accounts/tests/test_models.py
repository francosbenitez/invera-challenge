import pytest
from django.contrib.auth import get_user_model

from apps.accounts.tests.factories import UserFactory

User = get_user_model()


@pytest.mark.django_db
def test_user_model():
    UserFactory()
    assert User.objects.count() == 1
