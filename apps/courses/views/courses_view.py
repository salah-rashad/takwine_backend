from rest_framework import filters, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.custom_permissions import IsAdminUserOrReadOnly

from ..models import Course, CourseCategory, FeaturedCourse
from ..serializers import CourseCategorySerializer, CourseSerializer


class CoursesView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    search_fields = ['title', 'description',
                     'category__title', 'category__description', ]
    filter_backends = (filters.SearchFilter, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = self.queryset.filter(category=category)
        return queryset

    # # 1. List all
    # def get(self, request, *args, **kwargs):
    #     courses = Course.objects.all()
    #     serializer = CourseSerializer(courses, many=True)

    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # # 2. Create New
    # def post(self, request, *args, **kwargs):
    #     serializer = CourseSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # 2. Delete All
    # def delete(self, request, *args, **kwargs):
    #     Course.objects.all().delete()
    #     return Response(
    #         {
    #             "message": "All courses deleted!",
    #         }
    #     )


class CourseCategoriesView(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseCategorySerializer
    queryset = CourseCategory.objects.all()

    # # 1. List all
    # def get(self, request, *args, **kwargs):
    #     categories = CourseCategory.objects.all()
    #     serializer = CourseCategorySerializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class FeaturedCoursesView(APIView):
    def get(self, request, *args, **kwargs):
        objects = FeaturedCourse.objects.all()
        courses = list(map(lambda x: x.course, objects))
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
