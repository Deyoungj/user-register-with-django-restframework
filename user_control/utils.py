import jwt
from datetime import datetime
from django.conf import settings
from .models import CustomUser


def get_access_token(payload, day):
    token = jwt.encode(
        {'exp': datetime.now() + datetime.timedelta(days=1), **payload },
        key= settings.SECRET_KEY, algorithm='HS256'
    )
    return token


def decodeJWT(bearer):
    if not bearer:
        return None

    token = bearer[7:]

    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
    except Exception:
        return None

    if decoded:
        try:
            return CustomUser.objects.filter(id=decoded['user_id'])
        except:
            return None

