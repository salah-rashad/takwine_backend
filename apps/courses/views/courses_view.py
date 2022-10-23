from rest_framework import filters, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.custom_permissions import IsAdminUserOrReadOnly

from ..models.course import Course
from ..models.course_category import CourseCategory
from ..models.featured_course import FeaturedCourse
from ..serializers import CourseCategorySerializer, CourseSerializer


class CoursesView(generics.ListAPIView):
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


class CourseCategoriesView(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseCategorySerializer
    queryset = CourseCategory.objects.all()


class FeaturedCoursesView(APIView):
    def get(self, request, *args, **kwargs):
        featuredCourses = FeaturedCourse.objects.all()
        courses = list(map(lambda item: item.course, featuredCourses))
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
