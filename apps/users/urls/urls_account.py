from django.urls import path

from ..api.account import (CertificatesApiView, ChangePasswordApiView,
                           CompleteLessonsApiView, CourseBookmarksApiView,
                           DocumentBookmarksApiView, EnrollmentsApiView,
                           LastActivityApiView, ProfileApiView,
                           SingleCourseBookmarkApiView,
                           SingleDocumentBookmarkApiView,
                           SingleEnrollmentApiView,
                           SingleEnrollmentLessonsApiView,
                           UpdateProfileImageApiView, UserStatementsApiView)

# app_name = 'users'

urlpatterns = [
    path('profile', ProfileApiView.as_view()),
    path('change-password', ChangePasswordApiView.as_view()),
    path('update-profile-image', UpdateProfileImageApiView.as_view()),
    path("enrollments", EnrollmentsApiView.as_view()),
    path("enrollments/<int:pk>", SingleEnrollmentApiView.as_view()),
    path("enrollments/<int:pk>/lessons",
         SingleEnrollmentLessonsApiView.as_view()),
    path("enrollments/<int:pk>/complete-lessons",
         CompleteLessonsApiView.as_view()),
    path("enrollments/last-activity", LastActivityApiView.as_view()),
    path("statements", UserStatementsApiView.as_view()),
    path("certificates", CertificatesApiView.as_view()),
    path("course-bookmarks", CourseBookmarksApiView.as_view()),
    path("course-bookmarks/<int:pk>", SingleCourseBookmarkApiView.as_view()),
    path("document-bookmarks", DocumentBookmarksApiView.as_view()),
    path("document-bookmarks/<int:pk>", SingleDocumentBookmarkApiView.as_view()),
]
