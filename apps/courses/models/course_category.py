from colorfield.fields import ColorField
from django.db import models
from faicon.fields import FAIconField
from model_clone import CloneMixin


class CourseCategory(CloneMixin, models.Model):
    class Meta:
        db_table = "course_categories"
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'

    title = models.CharField(null=True, blank=False, default=None, max_length=255)
    description = models.CharField(null=True, blank=True, default=None, max_length=255)
    color = ColorField(null=True, blank=False, default="#C1C1C1")
    icon = FAIconField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
