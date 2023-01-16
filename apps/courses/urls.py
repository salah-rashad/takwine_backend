from django.urls import path

from .api.api_views import (CourseCategoriesApiView, CoursesApiView,
                            ExamApiView, FeaturedCoursesApiView,
                            SingleCourseApiView, SingleCourseLessonsApiView,
                            SingleMaterialApiView)

urlpatterns = [
    path("", CoursesApiView.as_view()),
    path("<int:pk>", SingleCourseApiView.as_view()),
    path("<int:pk>/lessons", SingleCourseLessonsApiView.as_view()),
    path("<int:c>/lessons/<int:l>/materials/<int:m>", SingleMaterialApiView.as_view()),
    path("<int:c>/lessons/<int:l>/exam", ExamApiView.as_view()),
    path("categories", CourseCategoriesApiView.as_view()),
    path("featured", FeaturedCoursesApiView.as_view()),
]
