import jwt

from utils.responses import TOKEN_EXPIRED, UNAUTHORIZED


def getUserToken(request):
    token = request.COOKIES.get('jwt')

    if not token:
        return UNAUTHORIZED

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return TOKEN_EXPIRED()

    return payload