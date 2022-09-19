from rest_framework import routers, urlpatterns
from django.urls import path, include
from .views import (
    CreateUserView,
    LoginView,
    UpdatePasswordView,
    MeView
)


routers = routers.DefaultRouter(trailing_slash=False)

routers.register('create-user', CreateUserView, 'create_user')
routers.register('login', LoginView, 'login')
routers.register('update-password', UpdatePasswordView, 'update_user')
routers.register('me', MeView, 'me')


urlpatterns = {
    path('',include(routers.urls))
}