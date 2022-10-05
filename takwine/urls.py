import apps.users.urls.urls_auth as auth_urls
import apps.users.urls.urls_account as account_urls
import apps.courses.urls as courses_urls
from django.contrib import admin
from django.urls import include, path

# from users.views.single_user_view import SingleUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # auth
    path("auth/", include(auth_urls)),

    # account
    path("account/", include(account_urls)),

    # courses
    path("api/courses/", include(courses_urls)),
]
