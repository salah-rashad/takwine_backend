from django.db import models
from colorfield.fields import ColorField


class CourseCategory(models.Model):
    class Meta:
        db_table = "courses_categories"
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'

    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, blank=True, max_length=255)
    description = models.CharField(null=False, blank=True, max_length=255)
    color = ColorField(null=False, blank=True, default="#C1C1C1")

    def __str__(self):
        return str(self.title)