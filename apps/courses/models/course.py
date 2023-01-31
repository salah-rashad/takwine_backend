from django.db import models
from django.forms import ValidationError
from model_clone import CloneMixin

from apps.users.models import Enrollment
from utils.validators import FileSizeValidator

from .course_category import CourseCategory
from .course_file import CourseFile
from .lesson import Lesson


class Course(CloneMixin, models.Model):
    class Meta:
        db_table = "courses"
        ordering = ['ordering', ]

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    title = models.CharField(null=True, blank=False, default=None, max_length=255)
    description = models.CharField(null=True, blank=True, default=None, max_length=255)
    category = models.ForeignKey(
        CourseCategory,
        on_delete=models.SET_NULL,
        db_column='category',
        null=True, blank=True, default=None,
    )
    imageUrl = models.ImageField(null=True, blank=True, default=None, max_length=255, upload_to='uploads/images/',
                                 validators=[FileSizeValidator(max_size=2)], help_text="* Maximum upload file size 2 MB.")
    guideFile = models.ForeignKey(CourseFile, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses")
    videoUrl = models.CharField(null=True, blank=True, default=None, max_length=255)
    date = models.DateTimeField(null=True, blank=False, auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def days(self):
        lessons = self.lessons().all()
        days = 0
        for lesson in lessons:
            days += lesson.days
        return days

    def lessons_count(self):
        return len(self.lessons().all())

    def totalEnrollments(self):
        enrollments = Enrollment.objects.filter(course__id=self.id)
        return enrollments.count()

    def lessons(self):
        list = Lesson.objects.filter(course__id=self.id).order_by("ordering")
        return list

    def __str__(self):
        return str(self.title)
