from random import choices
from django.forms import CharField
from rest_framework import serializers
from .models import Student,Package, PackageEnroled, GENDER_CHOICES


class CreateStudentSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    phone_number = serializers.CharField()
    address = serializers.CharField()


class CreatePackageSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=1000000, decimal_places=2)
    months = serializers.CharField()


class PackageEnrolmentSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    package_id = serializers.CharField()