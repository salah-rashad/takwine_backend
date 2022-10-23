from ..models.course import Course
from ..serializers import CourseSerializer, LessonSerializer
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.custom_permissions import IsAdminUserOrReadOnly


def getCourseOr404(self, pk):
    try:
        return Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response(
            {
                "message": "Course does not exist"
            },
            status=status.HTTP_404_NOT_FOUND
        )


class SingleCourseView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.filter()

    # def get(self, request, pk):
    #     object = self.getCourseOr404(pk)
    #     if type(object) is Response:
    #         return object

    #     serializer = CourseSerializer(object)
    #     return Response(serializer.data)


class SingleCourseLessonsView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, pk):
        object = getCourseOr404(self, pk)
        if type(object) is Response:
            return object

        serializer = LessonSerializer(object.lessons, many=True)
        return Response(serializer.data)
