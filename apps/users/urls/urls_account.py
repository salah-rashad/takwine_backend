from django.urls import path

from ..views.account_views import (ChangePasswordView, CompleteLessonsView,
                                   EnrollmentsView, LastActivityView,
                                   ProfileView, SingleEnrollmentView,
                                   UpdateProfileImageView, UserStatementsView, CertificateView)

# app_name = 'users'

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('change-password', ChangePasswordView.as_view()),
    path('update-profile-image', UpdateProfileImageView.as_view()),
    path("enrollments", EnrollmentsView.as_view()),
    path("enrollments/<int:pk>", SingleEnrollmentView.as_view()),
    path("enrollments/<int:pk>/complete-lessons", CompleteLessonsView.as_view()),
    path("enrollments/last-activity", LastActivityView.as_view()),
    path("statements", UserStatementsView.as_view()),
    path("certificate/<int:pk>", CertificateView.as_view()),
]
