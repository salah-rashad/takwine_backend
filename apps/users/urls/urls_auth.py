from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from ..api.auth import LoginApiView, LogoutApiView, RegistrationApiView

# app_name = 'users'

urlpatterns = [
    path('register', RegistrationApiView.as_view()),
    path('login', LoginApiView.as_view()),
    path('logout', LogoutApiView.as_view()),

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
