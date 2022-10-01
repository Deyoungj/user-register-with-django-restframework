from rest_framework.permissions import BasePermission
from user_control.utils import decodeJWT


class IsAuthenticatedCustom(BasePermission):
    
  def has_permission(self, request, view):
    print('isauthenticated')
    try:
      auth_token = request.Meta.get("HTTP_AUTHORIZATION",None)
      print(auth_token)
    except Exception:
      return False
    
    if not auth_token:
        return False

    user = decodeJWT(auth_token)

    if not user:
        return False

    request.user = user
    return True


