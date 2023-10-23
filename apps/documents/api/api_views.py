from rest_framework import filters, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.custom_permissions import IsAdminUserOrReadOnly

from ..models.document import Document
from ..models.document_category import DocumentCategory
from ..models.document_file import DocumentFile
from ..serializers import (DocumentCategorySerializer, DocumentFileSerializer,
                           DocumentSerializer)


class DocumentsApiView(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    search_fields = [
        'title',
        'content',
        'category__title',
        'category__description',
    ]
    filter_backends = [filters.SearchFilter]
    serializer_class = DocumentSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')

        if category is not None:
            queryset = Document.objects.filter(category=category)
        else:
            queryset = Document.objects.all()
        return queryset


class FeaturedFilesApiView(APIView):
    def get(self, request):
        list = DocumentFile.objects.all()
        # files = list(map(lambda item: item.document, list))
        serializer = DocumentFileSerializer(list, many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class SingleDocumentApiView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class DocumentCategoriesApiView(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = DocumentCategorySerializer
    queryset = DocumentCategory.objects.all()
