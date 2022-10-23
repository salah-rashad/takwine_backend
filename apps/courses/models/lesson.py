from django.db import models

from apps.courses.models.course import Course

from .intermediates import Rel_Lesson_Material


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['ordering', ]

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    title = models.CharField(null=False, blank=True, max_length=255)
    description = models.CharField(null=False, blank=True, max_length=255)
    days = models.PositiveIntegerField(null=False, blank=False, default=1)
    materials = models.ManyToManyField(
        to="courses.Material",
        related_name="lessons",
        blank=True,
        through=Rel_Lesson_Material,
    )

    def materials_count(self):
        return len(self.materials.all())

    def related_courses(self):
        courses = Course.objects.filter(
            lessons__id=self.id)
        return list(map(lambda x: x.title, courses))

    def __str__(self):
        return str(self.title)
