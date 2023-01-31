from django.db import models

from takwine.models import TakwineFile


class DocumentFile(TakwineFile):
    class Meta:
        db_table = "document_files"
        verbose_name = 'Document File'
        verbose_name_plural = 'Document Files'
        ordering = ['ordering']

    document = models.ForeignKey("documents.Document", on_delete=models.SET_NULL, null=True, blank=True)
