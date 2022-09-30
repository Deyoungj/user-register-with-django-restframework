from random import choices
from django.forms import CharField
from rest_framework import serializers
from .models import Student,Package, PackageEnroled


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = "__all__"

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"


# class PackageEnrolmentSerializer(serializers.Serializer):
#     user_id = serializers.CharField()
#     package_id = serializers.CharField()

class PackageEnrolmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageEnroled
        fields = "__all__"