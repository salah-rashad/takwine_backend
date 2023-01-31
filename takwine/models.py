from django.db import models
from model_clone import CloneMixin

from utils.validators import FileSizeValidator


class TakwineFile(CloneMixin, models.Model):
    class Meta:
        abstract = True
        db_table = "files"
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    name = models.CharField(null=False, blank=False, default="ملف", max_length=255)
    file = models.FileField(null=False, blank=False, upload_to='uploads/files/', validators=[FileSizeValidator(max_size=5)], help_text="* Maximum upload file size 5 MB.")
    date = models.DateTimeField(null=True, blank=False, auto_now_add=True)

    def __str__(self):
        return str(self.name)
