from colorfield.fields import ColorField
from django.db import models
from faicon.fields import FAIconField
from model_clone import CloneMixin


class DocumentCategory(CloneMixin, models.Model):
    class Meta:
        db_table = "document_categories"
        verbose_name = 'Document Category'
        verbose_name_plural = 'Document Categories'

    title = models.CharField(null=True, blank=False, default=None, max_length=255)
    description = models.CharField(null=True, blank=True, default=None, max_length=255)
    color = ColorField(null=True, blank=False, default="#C1C1C1")
    icon = FAIconField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
