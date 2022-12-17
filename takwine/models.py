from django.db import models
from django.forms import ValidationError


class TakwineFile(models.Model):
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

    def file_size_validator(value):
        limit = 5 * 1024 * 1024  # 5 MB
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 5 MiB.')

    name = models.CharField(null=False, blank=False, default="ملف", max_length=255)
    file = models.FileField(null=False, blank=False, upload_to='uploads/files/', validators=[file_size_validator], help_text="* Maximum upload file size 5 MB.")
    date = models.DateTimeField(null=True, blank=False, auto_now_add=True)

    def __str__(self):
        return str(self.name)
