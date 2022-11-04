import apps.courses.urls as courses_urls
import apps.users.urls.urls_account as account_urls
import apps.users.urls.urls_auth as auth_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.autodiscover()
# admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('summernote/', include('django_summernote.urls')),

    # auth
    path("auth/", include(auth_urls)),

    # account
    path("account/", include(account_urls)),

    # courses
    path("api/courses/", include(courses_urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
