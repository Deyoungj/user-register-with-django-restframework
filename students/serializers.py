from random import choices
from django.forms import CharField
from rest_framework import serializers
from .models import Student,Package, PackageEnroled, GENDER_CHOICES


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = "__all__"

class PackageSerializer(serializers.Serializer):
    class Meta:
        moodel = Package
        fields = "__all__"


class PackageEnrolmentSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    package_id = serializers.CharField()

class PackageEnrolmentedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageEnroled
        fields = "__all__"