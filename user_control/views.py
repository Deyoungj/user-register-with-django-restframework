from .utils import generate_user_tokens
from rest_framework.viewsets import ModelViewSet
from .serializers import (CreateUserSerializer,
                            CustomUser, LoginSerializer,
                            UpdatePasswordSerializer, CustomUserSerializer)
from rest_framework.response import Response
from django.contrib.auth import authenticate
from datetime import datetime
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny


class CreateUserView(ModelViewSet):
    http_method_names = ['post']
    serializer_class= CreateUserSerializer
    queryset = CustomUser.objects.all()
    # permission_classes = (IsAuthenticatedCustom,)

    def create(self, request):
        valid_request =  self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)
        print('User created: with data: '**valid_request)
        print('User created: with valid data: '**valid_request.validated_data)
        CustomUser.objects.create(**valid_request.validated_data)
        return Response(
            {"success":"User created successfully"},
            status=status.HTTP_201_CREATED
        )

class LoginView(ModelViewSet):
    http_method_names = ['post']
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny,]

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        user = authenticate(
            username= valid_request.validated_data["email"],
            password= valid_request.validated_data["password"]
        )
        print('user:', user)
        if not user:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        access = generate_user_tokens(user)
        print(access)

        user.last_login = timezone.now()
        user.save()

        return Response(access, status=status.HTTP_200_OK)
            

class UpdatePasswordView(ModelViewSet):
    http_method_names = ['post']
    serializer_class = UpdatePasswordSerializer
    queryset = CustomUser.objects.all()
    permission_classes= [IsAuthenticated,]

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        user = CustomUser.objects.filter(id= int(valid_request.validated_data["user_id"]))

        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        user = user[0]

        user.set_password(valid_request.validated_data["password"])
        user.save()

        return Response({'success': 'password changed successfully'})


class MeView(ModelViewSet):
    http_method_names = ['get']
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    # def list(self, request):
    #     data = self.serializer_class(data=request.data)
    #     return Response(data)
