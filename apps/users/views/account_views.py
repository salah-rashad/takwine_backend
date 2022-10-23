import json
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.helpers import getUserToken
from utils.responses import *

from ...courses.models.course import Course
from ..models import Enrollment, User
from ..serializers import EnrollmentSerializer, UserSerializer


class ProfileView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        user = User.objects.filter(id=token['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        # TODO: updating profile

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
    def put(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        pass


class EnrollmentsView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        list = Enrollment.objects.filter(
            user_id=token['id'])
        serializer = EnrollmentSerializer(list, many=True)
        return Response(serializer.data)

    def post(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        try:
            userId = token['id']
            courseId = request.data['course']
        except:
            raise

        filter = Enrollment.objects.filter(
            user=userId,
            course=courseId,
        )

        if (filter.exists()):
            ser = EnrollmentSerializer(filter.first())
            return Response(ser.data)

        request.data["user"] = userId

        serializer = EnrollmentSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class SingleEnrollmentView(APIView):
    def get(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        filter = Enrollment.objects.filter(
            user__id=token['id'],
            course__id=pk,
        )

        if (filter.exists()):
            obj = filter.first()
            serializer = EnrollmentSerializer(obj)
            data = serializer.data
        else:
            data = None

        return Response(data)


class LastActivityView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        list = Enrollment.objects.filter(
            user__id=token['id']).exclude(currentLesson=None)
        lastActivity = list.order_by('-updated_at').first()
        if (lastActivity):
            serializer = EnrollmentSerializer(lastActivity)
            return Response(serializer.data)
        else:
            return Response(
                {
                    "message": "Last course activity not found."
                }, status=status.HTTP_404_NOT_FOUND
            )


class UserStatementsView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        userId = token['id']

        enrollments = Enrollment.objects.filter(user__id=userId)

        completed = 0
        inProgress = 0

        for e in enrollments:
            if e.isComplete():
                completed += 1
            else:
                inProgress += 1

        rate = self.getCertificatesRateAverage(userId)

        return Response({
            "completed": completed,
            "inProgress": inProgress,
            "rate": rate,
        })

    def getCertificatesRateAverage(self, userId) -> str:
        return "3.5/5"     # TODO:
