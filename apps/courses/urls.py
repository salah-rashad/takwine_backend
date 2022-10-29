from django.urls import path
from apps.courses.views.courses_view import (
    CourseCategoriesView, CoursesView, FeaturedCoursesView,)
from apps.courses.views.single_course_view import (
    LessonExamView, SingleCourseLessonsView, SingleCourseView, LessonSingleMaterialView)

urlpatterns = [
    path("", CoursesView.as_view()),
    path("<int:pk>", SingleCourseView.as_view()),
    path("<int:pk>/lessons", SingleCourseLessonsView.as_view()),
    path("<int:c>/lessons/<int:l>/materials/<int:m>",
         LessonSingleMaterialView.as_view()),
    path("<int:c>/lessons/<int:l>/exam", LessonExamView.as_view()),
    path("categories", CourseCategoriesView.as_view()),
    path("featured", FeaturedCoursesView.as_view()),
]
