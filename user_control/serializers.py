from rest_framework import serializers
from .models import CustomUser, Role


class CustomUserSerializer(serializers.Serializer):
    fullname = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=Role)