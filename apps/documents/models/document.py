from django.core.validators import FileExtensionValidator
from django.db import models
from django.forms import ValidationError

from apps.documents.models.document_file import DocumentFile
from utils.validators import FileSizeValidator

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
    imageUrl = models.ImageField(null=True, blank=True, default=None, max_length=255, upload_to='uploads/images/',
                                 validators=[FileSizeValidator(max_size=2)], help_text="* Maximum upload file size 2 MB.")
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
