from rest_framework.viewsets import ModelViewSet
from .serializers import CreateUserSerializer, CustomUser
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(ModelViewSet):
    http_method_names = ['post']
    serializer_class= CreateUserSerializer
    queryset = CustomUser.objects.all()

    def create(self, request):
        valid_request =  self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        CustomUser.objects.create(**valid_request.validated_data)
        return Response(
            {"success":"User created successfully"},
            status=status.HTTP_201_CREATED
        )