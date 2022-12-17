from django.core.validators import FileExtensionValidator
from django.db import models

from apps.documents.models.document_file import DocumentFile

from .document_category import DocumentCategory


class Document(models.Model):
    class Meta:
        db_table = "documents"
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    title = models.CharField(null=True, blank=False, default=None, max_length=255)
    imageUrl = models.ImageField(null=True, blank=True, default=None, max_length=255, upload_to='uploads/images/')
    category = models.ForeignKey(
        DocumentCategory,
        on_delete=models.SET_NULL,
        db_column='category',
        null=True, blank=True, default=None,
    )
    date = models.DateTimeField(null=True, blank=False, auto_now_add=True)
    enabled = models.BooleanField(default=True)
    content = models.TextField(null=True, blank=True)

    @property
    def files(self):
        list = DocumentFile.objects.filter(document=self)
        return list
    
    def __str__(self) -> str:
        return str(self.title)
