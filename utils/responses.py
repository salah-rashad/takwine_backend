from rest_framework import status
from rest_framework.response import Response

# class AuthResponse(Response):
#     error: bool
#     message: Any

#     def __init__(self, message: Any, error=False, status=status.HTTP_200_OK):
#         self.error = error
#         self.message = message
#         self.status_code = status
#         super().__init__(
#             data={
#                 "error": self.error,
#                 "message": self.message
#             },
#             status=self.status_code,
#         )

INVALID_CREDENTIALS = Response(
    {
        "message": "بيانات الدخول غير صحيحة."
    },
    status=status.HTTP_400_BAD_REQUEST
)

UNAUTHORIZED = Response(
    {
        "message": "غير مسموح."
    },
    status=status.HTTP_401_UNAUTHORIZED
)


def TOKEN_EXPIRED(deleteJwt: bool = True):
    response = Response()
    response.data = {
        "message": "غير مسموح، انتهت صلاحية الدخول."
    },
    response.status = status.HTTP_401_UNAUTHORIZED,
    if deleteJwt:
        response.delete_cookie('jwt')

    return response
