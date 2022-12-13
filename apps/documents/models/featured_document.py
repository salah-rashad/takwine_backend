from django.db import models

from .document import Document


class FeaturedDocument(models.Model):
    class Meta:
        db_table = "documents_featured"
        verbose_name = 'Featured Document'
        verbose_name_plural = 'Featured Documents'
        ordering = ['ordering']

    document = models.OneToOneField(
        Document, on_delete=models.CASCADE, unique=True)

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    def __str__(self):
        return str(self.document.title)
