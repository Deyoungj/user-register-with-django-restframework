from rest_framework import routers
from .views import (
    CreateUserView,
    LoginView,
    UpdatePasswordView,
    MeView
)


route = routers.DefaultRouter(trailing_slash=False)

route.register('create-user', CreateUserView, 'create_user')
route.register('login', LoginView, 'login')
route.register('update-password', UpdatePasswordView, 'update_user')
route.register('me', MeView, 'me')