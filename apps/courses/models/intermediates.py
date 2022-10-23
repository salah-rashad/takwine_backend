from django.db import models


class Rel_Course_Lesson(models.Model):
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        db_table = "_course_lesson_"
        ordering = ['ordering', ]
        unique_together = ('course', 'lesson',)

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE,)
    lesson = models.ForeignKey("courses.Lesson", on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.lesson)


class Rel_Lesson_Material(models.Model):
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        db_table = "_lesson_material_"
        ordering = ['ordering', ]
        unique_together = ('lesson', 'material',)

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    lesson = models.ForeignKey("courses.Lesson", on_delete=models.CASCADE,)
    material = models.ForeignKey("courses.Material", on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.material)


class Rel_Material_Component(models.Model):
    class Meta:
        verbose_name = 'Component'
        verbose_name_plural = 'Components'
        db_table = "_material_component_"
        ordering = ['ordering', ]
        unique_together = ('material', 'component',)

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    material = models.ForeignKey("courses.Material", on_delete=models.CASCADE,)
    component = models.ForeignKey(
        "courses.MaterialComponent", on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.component)


class Rel_Material_Attachment(models.Model):
    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'
        db_table = "_material_attachment_"
        ordering = ['ordering', ]
        unique_together = ('material', 'attachment',)

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    material = models.ForeignKey("courses.Material", on_delete=models.CASCADE,)
    attachment = models.ForeignKey(
        "courses.MaterialAttachment", on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.attachment)
