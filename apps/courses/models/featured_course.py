from django.db import models

from .course import Course


class FeaturedCourse(models.Model):
    class Meta:
        db_table = "courses_featured"
        verbose_name = 'Featured Course'
        verbose_name_plural = 'Featured Courses'
        ordering = ['ordering']

    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, unique=True)

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    def __str__(self):
        return str(self.course.title)
