from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateStudentSerializer, CreatePackageSerializer, PackageEnrolmentSerializer
from .models import Student, Package, PackageEnroled
 
class StudentView(ModelViewSet):
    # http_method_names = ['post']
    serializer_class = CreateStudentSerializer
    queryset = Student.objects.all()
    
    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        print(**valid_request.validated_data)

        Student.objects.create(**valid_request.validated_data)

        return Response(
            {'success':'student created successfully'},
            status=status.HTTP_201_CREATED
        )


class PackageView(ModelViewSet):
    http_method_names = ['post', 'get']
    queryset = Package.objects.all()
    serializer_class = CreatePackageSerializer

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        Package.objects.create(**valid_request.validated_data)

        return Response(
            {'success': 'package created successfully'},
            status=status.HTTP_201_CREATED
        )

class EnrollStudentView(ModelViewSet):
    http_method_names = ['post']
    serializer_class = PackageEnrolmentSerializer
    queryset = PackageEnroled.objects.all()

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        PackageEnroled.objects.create(
            package=valid_request.validated_data['package_id'],
            student= valid_request.validated_data['user_id']
        )

        return Response(
            {'success': 'enrolled student success'},
            status = status.HTTP_201_CREATED
        )



