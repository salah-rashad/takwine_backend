from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.helpers import getUserToken
from utils.responses import INVALID_CREDENTIALS

from apps.courses.serializers import LessonSerializer
from apps.users.models import (Certificate, CourseBookmark, DocumentBookmark,
                      Enrollment, User)
from ..serializers import (CertificateSerializer, ChangePasswordSerializer,
                           CompleteLessonSerializer, CourseBookmarkSerializer,
                           DocumentBookmarkSerializer, EnrollmentSerializer,
                           UserSerializer)


class ProfileApiView(APIView):
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

        try:
            userId = token['id']
            user = User.objects.filter(id=userId).first()
        except:
            raise

        newSerializer = UserSerializer(user, data=request.data, partial=True)
        newSerializer.is_valid(raise_exception=True)
        newSerializer.save()
        return Response(newSerializer.data, status=status.HTTP_200_OK)


class ChangePasswordApiView(APIView):
    def put(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        # check login credentials and request data
        try:
            userId = token['id']
            user: User = User.objects.filter(id=userId).first()
            oldPassword = request.data['oldPassword']
            newPassword = request.data['newPassword']

            if user == None:
                raise

            # check if old password matches the current user's password
            if not user.check_password(oldPassword):
                return Response(
                    {
                        "oldPassword": "كلمة المرور الحالية غير صحيحة."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return INVALID_CREDENTIALS

        try:
            validate_password(newPassword)

            user.set_password(newPassword)
            user.save()
            return Response(
                {
                    "message": "تم تغيير كلمة المرور."
                },
                status=status.HTTP_200_OK
            )
        except ValidationError as error:
            return Response({"newPassword": error}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {
                    "message": "حدث خطأ ما أثناء تغيير كلمة المرور، يرجى التأكد من البيانات."
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class EnrollmentsApiView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        list = Enrollment.objects.filter(
            user=token['id']).order_by("updated_at")
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

        enrollment = Enrollment.objects.filter(
            user=userId,
            course=courseId,
        ).first()

        if enrollment:
            serializer = EnrollmentSerializer(enrollment)
            return Response(serializer.data)

        data = {}
        data = dict(request.data)
        data["user"] = userId

        serializer = EnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class SingleEnrollmentApiView(APIView):
    def get(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        enrollment = Enrollment.objects.filter(
            user=token['id'],
            course=pk,
        ).first()

        if enrollment:
            serializer = EnrollmentSerializer(enrollment)
            data = serializer.data
        else:
            data = None

        return Response(data)


class SingleEnrollmentLessonsApiView(APIView):
    def get(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        enrollment = Enrollment.objects.filter(
            user=token['id'],
            course=pk,
        ).first()

        if enrollment:
            data = []

            lessons = enrollment.course.lessons().order_by('ordering')
            complete = enrollment.completeLessons()
            completeList = list(
                map(lambda x: x.lesson, complete))

            for item in lessons:
                lessonData = LessonSerializer(item).data
                if item in completeList:
                    result = complete.filter(lesson=item).first().result
                    lessonData.update({"isComplete": True, "result": result})
                data.append(lessonData)
        else:
            data = None

        return Response(data)


class LastActivityApiView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        list = Enrollment.objects.filter(user=token['id'])
        lastActivity = list.order_by('-updated_at').first()
        if (lastActivity):
            serializer = EnrollmentSerializer(lastActivity)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        try:
            courseId = request.data['course']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        enrollment = Enrollment.objects.filter(
            user=token['id'],
            course=courseId,
        ).first()

        if enrollment:
            # enrollment.updated_at = datetime.now()
            enrollment.save()
            serializer = EnrollmentSerializer(enrollment)
            return Response(serializer.data)

        return Response(status=status.HTTP_304_NOT_MODIFIED)


class UserStatementsApiView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        userId = token['id']

        enrollments = Enrollment.objects.filter(user=userId)

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

    def getCertificatesRateAverage(self, userId) -> str | None:
        certificates = Certificate.objects.filter(user=userId)

        if not certificates:
            return None

        total_sum = 0
        for cert in certificates:
            total_sum += cert.result

        avarage = total_sum / len(certificates)
        rate = (avarage / 100) * 5
        return "{0:.1f}/5".format(rate)


class CompleteLessonsApiView(APIView):
    def get(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        enrollment = Enrollment.objects.filter(
            user=token['id'],
            course=pk,
        ).first()

        if enrollment:
            list = enrollment.completeLessons()
            serializer = CompleteLessonSerializer(list, many=True)
            return Response(serializer.data)

    def post(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        try:
            lessonId = request.data['lesson']
            result = request.data['result']
        except:
            raise

        enrollment = Enrollment.objects.filter(
            user=token['id'],
            course=pk,
        ).first()

        if enrollment is not None:
            completeLesson = enrollment.completeLessons().filter(lesson=lessonId).first()

            response = None

            # if object is already exists
            if completeLesson:
                # if result is null then update it
                if completeLesson.result == None:
                    completeLesson.result = result
                    completeLesson.save()
                    response = Response({
                        "message": "Lesson added successfully"
                    })
                else:
                    completeLesson.save()
                    response = Response({
                        "message": "Lesson already added"
                    })

            # if object doesn't exist create a new one
            data = {}
            data = dict(request.data)
            data["enrollment"] = enrollment.id
            serializer = CompleteLessonSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response = Response(
                    serializer.data, status=status.HTTP_201_CREATED)
            else:
                response = Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            # update enrollment
            enrollment.save()
            return response

        return Response(
            {
                "message": "Error while updating enrollment lesson"
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class CertificatesApiView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        list = Certificate.objects.filter(user=token['id'])
        serializer = CertificateSerializer(list, many=True)
        return Response(serializer.data)


class CourseBookmarksApiView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        list = CourseBookmark.objects.filter(user=token['id']).order_by("id")
        serializer = CourseBookmarkSerializer(list, many=True)
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

        bookmark = CourseBookmark.objects.filter(
            user=userId,
            course=courseId,
        ).first()

        if bookmark:
            serializer = CourseBookmarkSerializer(bookmark)
            return Response(serializer.data)

        data = {}
        data = dict(request.data)
        data["user"] = userId
        data["course"] = courseId

        serializer = CourseBookmarkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class SingleCourseBookmarkApiView(APIView):
    def get(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        bookmark = CourseBookmark.objects.filter(
            user=token['id'],
            course=pk,
        ).first()

        if bookmark:
            serializer = CourseBookmarkSerializer(bookmark)
            return Response(serializer.data)
        else:
            return Response(
                {"message": "Course bookmark not found!"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        bookmark = CourseBookmark.objects.filter(
            user=token['id'],
            course=pk,
        ).first()

        if bookmark:
            bookmark.delete()

        return Response(
            {"message": "Course bookmark removed!"},
            status=status.HTTP_200_OK
        )


class DocumentBookmarksApiView(APIView):
    def get(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        list = DocumentBookmark.objects.filter(user=token['id']).order_by("id")
        serializer = DocumentBookmarkSerializer(list, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        try:
            userId = token['id']
            documentId = request.data['document']
        except:
            raise

        bookmark = DocumentBookmark.objects.filter(
            user=userId,
            document=documentId,
        ).first()

        if bookmark:
            serializer = DocumentBookmarkSerializer(bookmark, context={'request': request})
            return Response(serializer.data)

        data = {}
        data = dict(request.data)
        data["user"] = userId
        data["document"] = documentId

        serializer = DocumentBookmarkSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class SingleDocumentBookmarkApiView(APIView):
    def get(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        bookmark = DocumentBookmark.objects.filter(
            user=token['id'],
            document=pk,
        ).first()

        if bookmark:
            serializer = DocumentBookmarkSerializer(bookmark)
            return Response(serializer.data)
        else:
            return Response(
                {"message": "Document bookmark not found!"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        token = getUserToken(request)

        if type(token) is Response:
            return token

        bookmark = DocumentBookmark.objects.filter(
            user=token['id'],
            document=pk,
        ).first()

        if bookmark:
            bookmark.delete()

        return Response(
            {"message": "Document bookmark removed!"},
            status=status.HTTP_200_OK
        )
