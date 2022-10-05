from ..models import Course
from ..serializers import CourseSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.custom_permissions import IsAdminUserOrReadOnly


class SingleCourseView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def getCourseOr404(self, pk):
        try:
            return Course.objects.get(id=pk)
        except Course.DoesNotExist:
            return Response(
                {
                    "error": "Course does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk, *args, **kwargs):
        object = self.getCourseOr404(pk)
        if type(object) is Response:
            return object

        serializer = CourseSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        object = self.getCourseOr404(pk)
        if type(object) is Response:
            return object

        request.data['id'] = pk
        serializer = CourseSerializer(instance=object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        object = self.getCourseOr404(pk)
        if type(object) is Response:
            return object

        object.delete()
        return Response(
            {
                "message": "Course deleted!"
            }
        )
