from rest_framework import serializers
from .models import CustomUser, Role


class CreateUserSerializer(serializers.Serializer):
    fullname = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=Role)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()