from django.urls import path
from apps.courses.views.courses_view import (
    CourseCategoriesView, CoursesView, FeaturedCoursesView,)
from apps.courses.views.single_course_view import SingleCourseView

urlpatterns = [
    path("", CoursesView.as_view()),
    path("<int:pk>", SingleCourseView.as_view()),
    path("categories", CourseCategoriesView.as_view()),
    path("featured", FeaturedCoursesView.as_view()),
]
