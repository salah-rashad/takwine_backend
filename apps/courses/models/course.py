from django.db import models

from apps.users.models import Enrollment

from .intermediates import Rel_Course_Lesson

from .course_category import CourseCategory


class Course(models.Model):
    class Meta:
        db_table = "courses"
        ordering = ['ordering', ]

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.CharField(null=False, blank=True, max_length=255)
    category = models.ForeignKey(
        CourseCategory,
        on_delete=models.RESTRICT,
        db_column='category',
        blank=False, null=False,
    )
    imageUrl = models.CharField(null=False, blank=True, max_length=255)
    pdfUrl = models.CharField(null=False, blank=True, max_length=255)
    videoUrl = models.CharField(null=False, blank=True, max_length=255)
    date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    enabled = models.BooleanField(default=True)
    lessons = models.ManyToManyField(
        to="courses.Lesson",
        related_name="courses",
        blank=True,
        through=Rel_Course_Lesson,
    )

    def days(self):
        lessons = self.lessons.all()
        days = 0
        for lesson in lessons:
            days += lesson.days
        return days

    def lessons_count(self):
        return len(self.lessons.all())

    def totalEnrollments(self):
        enrollments = Enrollment.objects.filter(course__id=self.id)
        return enrollments.count()

    def __str__(self):
        return str(self.title)
