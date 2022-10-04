import jwt
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings
from .models import CustomUser


def get_access_token(payload, days):
    token = jwt.encode(
        {'exp': timezone.now() + timedelta(days=days), **payload },
        key= settings.SECRET_KEY, algorithm='HS256'
    )
    return token


def decodeJWT(bearer):
    if not bearer:
        return None

    token = bearer[7:]
    print('Decoding token', token)

    try:
        decoded = jwt.decode(token, key= settings.SECRET_KEY, algorithm='HS256')
        print('Decoded bool token', decoded)
    except Exception:
        return None

    if decoded:
        try:
            return CustomUser.objects.filter(id=decoded['user_id'])
        except:
            return None

