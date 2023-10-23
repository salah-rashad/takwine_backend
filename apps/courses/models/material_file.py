from takwine.models import TakwineFile
from django.db import models


class MaterialFile(TakwineFile):
    class Meta:
        db_table = "material_files"
        verbose_name = 'Material File'
        verbose_name_plural = 'Material Files'
        ordering = ['ordering']

    material = models.ForeignKey("Material", on_delete=models.SET_NULL, null=True, blank=True)
