from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "name",
            "first_name",
            "last_name",
        ]

    def get_name(self, obj):
        return obj.get_full_name()


class RegisterUserSerializer(RegisterSerializer):
    """
    Serializer for the User model with first_name and last_name fields.
    """

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["first_name"] = self.validated_data.get("first_name", "")
        data_dict["last_name"] = self.validated_data.get("last_name", "")

        return data_dict

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get("first_name")
        user.last_name = self.data.get("last_name")
        user.save()

        return user

    def validate_password1(self, password1):
        password_minimum_length = 8

        if len(password1) < password_minimum_length:
            raise serializers.ValidationError(
                f"La longitud mínima de contraseña permitida es {password_minimum_length}."
            )

        return password1
