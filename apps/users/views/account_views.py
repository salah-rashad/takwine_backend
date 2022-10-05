from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.helpers import getUserToken
from utils.responses import *

from ..models import User
from ..serializers import UserSerializer


class ProfileView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        user = User.objects.filter(id=token['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        pass


class ChangePasswordView(APIView):
    def post(self, request):

        # check login credentials
        try:
            email = request.data['email']
            oldPassword = request.data['password']
            newPassword: str = request.data['newPassword']

            user = User.objects.filter(email=email).first()
            if user is None:
                raise
            if not user.check_password(oldPassword):
                raise
        except:
            return INVALID_CREDENTIALS

        try:
            validate_password(newPassword)

            user = User.objects.filter(email=email).first()
            user.set_password(newPassword)
            user.save()
            return Response(
                {
                    "message": "Password changed successfully."
                },
                status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response({"New Password": e}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {
                    "message": "An error occurred while changing your password, please check your new password."
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class UpdateProfileImageView(APIView):
    def put(self, request, *args, **kwargs):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        pass


class EnrolledCoursesView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # serializer_class = CourseCategorySerializer
    # queryset = CourseCategory.objects.all()
