from ast import Is
from rest_framework.viewsets import ModelViewSet
from .serializers import (CreateUserSerializer,
 CustomUser, LoginSerializer,
  UpdatePasswordSerializer, CustomUserSerializer)
from rest_framework.response import Response
from django.contrib.auth import authenticate
from datetime import datetime
from rest_framework import status
from .utils import get_access_token
from teamCSG.custom_method import IsAuthenticatedCustom


class CreateUserView(ModelViewSet):
    http_method_names = ['post']
    serializer_class= CreateUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticatedCustom,)

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

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        new_user = valid_request.validated_data["is_new_user"]

        if new_user:
            user = CustomUser.objects.filter(email = valid_request.validated_data["email"])

            if user:
                user = user[0]
                if not user.password:
                    return Response({'user_id': user.id})
                else:
                    raise Exception('user already has Password')

        user = authenticate(
            username= valid_request.validated_data["email"],
            password= valid_request.validated_data["password"]
        )
            
        if not user:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        access = get_access_token({'user_id': user.id},1)

        user.last_login = datetime.now()
        user.save()

        return Response({'access': access}, status=status.HTTP_200_OK)
            

class UpdatePasswordView(ModelViewSet):
    http_method_names = ['post']
    serializer_class = UpdatePasswordSerializer
    queryset = CustomUser.objects.all()

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        user = CustomUser.objects.filter(id=valid_request.validated_data["user_id"]).first()

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
    permission_classes = (IsAuthenticatedCustom,)

    # def list(self, request):
    #     data = self.serializer_class(data=request.data)
    #     return Response(data)
