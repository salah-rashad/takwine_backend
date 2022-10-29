from django.db import models


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

    lesson = models.ForeignKey("courses.Lesson", on_delete=models.CASCADE)

    title = models.CharField(null=False, blank=False, max_length=255)
    content = models.TextField(null=True, blank=True)

    # components = models.ManyToManyField(
    #     to="courses.MaterialComponent",
    #     related_name="materials",
    #     blank=True,
    #     through=Rel_Material_Component,
    # )
    # attachments = models.ManyToManyField(
    #     to="courses.MaterialAttachment",
    #     related_name="materials",
    #     blank=True,
    #     through=Rel_Material_Attachment,
    # )

    # def components_count(self):
    #     return len(self.components().all())

    # def attachments_count(self):
    #     return len(self.attachments().all())

    # def components(self):
    #     list = MaterialComponent.objects.filter(material__id=self.id)
    #     return list

    # def attachments(self):
    #     list = MaterialAttachment.objects.filter(material__id=self.id)
    #     return list

    def __str__(self):
        return str(self.title)
