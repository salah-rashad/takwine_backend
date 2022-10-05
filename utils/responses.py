from rest_framework import status
from rest_framework.response import Response

INVALID_CREDENTIALS = Response(
    {
        "message": "Invalid credentials."
    },
    status=status.HTTP_400_BAD_REQUEST
)

UNAUTHORIZED = Response(
    {
        "message": "Access denied."
    },
    status=status.HTTP_401_UNAUTHORIZED
)


def TOKEN_EXPIRED(deleteJwt: bool = True):
    response = Response()
    response.data = {
        "message": "Access denied, session expired."
    },
    response.status = status.HTTP_401_UNAUTHORIZED,
    if deleteJwt:
        response.delete_cookie('jwt')

    return response
