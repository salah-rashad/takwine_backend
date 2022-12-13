from django.urls import path

from .api.api_views import (DocumentCategoriesApiView,
                            DocumentsApiView, FeaturedFilesApiView,
                            SingleDocumentApiView)

urlpatterns = [
    path("", DocumentsApiView.as_view()),
    path("<int:pk>", SingleDocumentApiView.as_view()),
    path("categories", DocumentCategoriesApiView.as_view()),
    path("featured", FeaturedFilesApiView.as_view()),
]
