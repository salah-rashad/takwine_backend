from django.db import models
from model_clone import CloneMixin

from .material_file import MaterialFile


class Material(CloneMixin, models.Model):
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    lesson = models.ForeignKey("courses.Lesson", on_delete=models.CASCADE)

    title = models.CharField(null=False, blank=False, max_length=255)
    content = models.TextField(null=True, blank=True)

    @property
    def files(self):
        list = MaterialFile.objects.filter(material=self)
        return list

    def __str__(self):
        return str(self.title)
