import factory
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
    is_active = True
    is_admin = False
    is_staff = False
    created_at = factory.LazyFunction(timezone.now)
    updated_at = factory.LazyFunction(timezone.now)

    @factory.post_generation
    def tasks(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for task in extracted:
                self.tasks.add(task)
