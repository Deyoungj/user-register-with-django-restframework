import jwt
from datetime import datetime
from django.conf import settings

def get_access_token(payload, day):
    token = jwt.encode(
        {'exp': datetime.now() + datetime.timedelta(days=1), **payload },
        key= settings.SECRET_KEY, algorithm='HS256'
    )
    return token