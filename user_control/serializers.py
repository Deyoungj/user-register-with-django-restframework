from rest_framework import serializers
from .models import CustomUser, Role


class CreateUserSerializer(serializers.Serializer):
    fullname = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=Role)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=False)
    is_new_user = serializers.BooleanField(default=False, required=False)


class UpdatePasswordSerializer(serializers.serializers):
    user_id = serializers.CharField()
    password = serializers.CharField()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"