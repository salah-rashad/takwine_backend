from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import apps.courses.urls as courses_urls
import apps.documents.urls as docs_urls
import apps.users.urls.urls_account as account_urls
import apps.users.urls.urls_auth as auth_urls
from apps.users.views import CertificateView

admin.autodiscover()
# admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('summernote/', include('django_summernote.urls')),
    path('faicon/', include('faicon.urls')),

    ########## API ##########
    path("api/auth/", include(auth_urls)),
    path("api/account/", include(account_urls)),
    path("api/courses/", include(courses_urls)),
    path("api/documents/", include(docs_urls)),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


    ########## VIEWS ##########
    path("certificate/<int:pk>", CertificateView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
