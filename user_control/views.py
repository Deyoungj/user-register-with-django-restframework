from rest_framework.viewsets import ModelViewSet
from .serializers import CreateUserSerializer, CustomUser, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status

class UserViewSet(ModelViewSet):
    http_method_names = ['post']
    serializer_class= CreateUserSerializer
    queryset = CustomUser.objects.all()

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

class LoginViewset(ModelViewSet):
    http_method_names = ['post']
    serializer_class = LoginSerializer()
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
            password= valid_request.validated_data("password",None)
        )
            
        if not user:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        access = get_access_token({'user_id': user_id}, )
            


