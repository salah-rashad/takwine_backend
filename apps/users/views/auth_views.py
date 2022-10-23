import datetime

import jwt
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.helpers import getUserToken
from utils.responses import *

from ..models import User
from ..serializers import UserSerializer

# Create your views here.


class RegistrationView(APIView):
    def post(self, request):

        errors = {}

        # validate password
        try:
            password = request.data.get('password')
            validate_password(password)
        except ValidationError as e:
            errors = {"password": e}
        except:
            pass

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Return a response with errors if they exist.
            if len(errors) > 0:
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)

            # If there are no errors, save the data and return it.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If the serializer is not valid, update errors with serializer's errors.
        errors.update(serializer.errors)

        # Return a response with all the errors.
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):

        # token = getUserToken(request)

        # if isinstance(token, dict):
        #     return Response(
        #         {
        #             "message": "You are already logged in."
        #         },
        #         status=status.HTTP_200_OK
        #     )

        try:
            email = request.data['email']
            password = request.data['password']

        except:
            return INVALID_CREDENTIALS

        user = User.objects.filter(email=email).first()
        if user is None:
            return INVALID_CREDENTIALS
        if not user.check_password(password):
            return INVALID_CREDENTIALS

        try:
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow(),
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()

            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                "message": "Logged in successfully."
            }
            response.status_code = status.HTTP_200_OK

            return response
        except:
            return Response(
                {
                    "message": "An error occurred while trying to log in."
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "Logged out successfully."
        }
        return response
