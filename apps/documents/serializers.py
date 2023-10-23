from rest_framework import serializers

from takwine.serializers import TakwineFileSerializer

from .models.document import Document
from .models.document_category import DocumentCategory
from .models.document_file import DocumentFile


class DocumentCategorySerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = DocumentCategory
        fields = "__all__"

    def get_icon(self, instance: DocumentCategory):
        icon = instance.icon
        return str(icon).split("icon:")[1]


class DocumentFileSerializer(TakwineFileSerializer):
    class Meta:
        model = DocumentFile
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    category = DocumentCategorySerializer()
    files = DocumentFileSerializer(many=True)

    class Meta:
        model = Document
        fields = "__all__"
