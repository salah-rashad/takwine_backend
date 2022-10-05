from django.urls import path

from ..views.account_views import (ChangePasswordView, EnrolledCoursesView,
                                   ProfileView, UpdateProfileImageView)

# app_name = 'users'

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('change-password', ChangePasswordView.as_view()),
    path('update-profile-image', UpdateProfileImageView.as_view()),
    path("enrolled-courses", EnrolledCoursesView().as_view()),
]
