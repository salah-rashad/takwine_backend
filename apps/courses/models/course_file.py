from takwine.models import TakwineFile
from django.db import models


class CourseFile(TakwineFile):
    class Meta:
        db_table = "course_files"
        verbose_name = 'Course File'
        verbose_name_plural = 'Course Files'

    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True, blank=True)
