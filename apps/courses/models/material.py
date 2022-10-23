from django.db import models

from .intermediates import Rel_Material_Attachment, Rel_Material_Component


class Material(models.Model):
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
    title = models.CharField(null=False, blank=True, max_length=255)

    components = models.ManyToManyField(
        to="courses.MaterialComponent",
        related_name="materials",
        blank=True,
        through=Rel_Material_Component,
    )
    attachments = models.ManyToManyField(
        to="courses.MaterialAttachment",
        related_name="materials",
        blank=True,
        through=Rel_Material_Attachment,
    )
    
    def components_count(self):
        return len(self.components.all())
    
    def attachments_count(self):
        return len(self.attachments.all())

    def __str__(self):
        return str(self.title)
