import factory
import faker
from django.contrib.auth import get_user_model
from django.utils import timezone
from factory.django import DjangoModelFactory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    """
    Factory for creating sample users.
    """

    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall(
        "set_password",
        faker.Faker().password(
            length=20,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ),
    )
    is_active = True
    is_admin = False
    is_staff = False
    created_at = factory.LazyFunction(timezone.now)
    updated_at = factory.LazyFunction(timezone.now)
