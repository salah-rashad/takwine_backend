from rest_framework import filters, generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.courses.models.exam import Exam

from apps.courses.models.lesson import Lesson
from utils.custom_permissions import IsAdminUserOrReadOnly

from ..models.course import Course
from ..models.course_category import CourseCategory
from ..models.featured_course import FeaturedCourse
from ..serializers import (CourseCategorySerializer, CourseSerializer,
                           ExamSerializer, LessonSerializer,
                           MaterialSerializer)


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


class CoursesApiView(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    search_fields = [
        'title',
        'description',
        'category__title',
        'category__description',
    ]
    filter_backends = [filters.SearchFilter]
    serializer_class = CourseSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')

        if category is not None:
            queryset = Course.objects.filter(category=category)
        else:
            queryset = Course.objects.all()
        return queryset


class CourseCategoriesApiView(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseCategorySerializer
    queryset = CourseCategory.objects.all()


class FeaturedCoursesApiView(APIView):
    def get(self, request, *args, **kwargs):
        featuredCourses = FeaturedCourse.objects.all()
        courses = list(map(lambda item: item.course, featuredCourses))
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SingleCourseApiView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.filter()

    # def get(self, request, pk):
    #     object = self.getCourseOr404(pk)
    #     if type(object) is Response:
    #         return object

    #     serializer = CourseSerializer(object)
    #     return Response(serializer.data)


class SingleCourseLessonsApiView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, pk):
        object = getCourseOr404(self, pk)
        if type(object) is Response:
            return object

        serializer = LessonSerializer(object.lessons(), many=True)
        return Response(serializer.data)


class SingleMaterialApiView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, c, l, m):

        lesson = Lesson.objects.filter(id=l).first()
        try:
            material = lesson.materials()[m]
            serializer = MaterialSerializer(material, context={'request': request})
            return Response(serializer.data)
        except:
            raise
            return Response(
                {
                    "message": "المادة غير موجودة.",
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ExamApiView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, c, l):

        exam = Exam.objects.filter(lesson=l).first()

        if exam:
            serializer = ExamSerializer(exam)
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)
