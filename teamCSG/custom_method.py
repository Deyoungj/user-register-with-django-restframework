from rest_framework.permissions import BasePermission
from user_control.utils import decodeJWT


class IsAuthenticatedCustom(BasePermission):
    
  def has_permission(self, request, view):
    print('isauthenticated')
    # print(request.user)
    try:
      auth_token = request.headers.get('Authorization')
      print(auth_token)
    except Exception:
      # print(Exception)
      return False
    
    if not auth_token:
        return False

    user = decodeJWT(auth_token)

    if not user:
        return False

    request.user = user
    return True


