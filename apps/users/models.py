import pathlib
from datetime import datetime

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe

from utils.storage import OverwriteStorage
from utils.validators import FileSizeValidator

from .managers import UserManager

GENDER_CHOICES = (
    ("m", "Male"),
    ("f", "Female")
)


class User(AbstractUser, PermissionsMixin):
    class Meta:
        db_table = "users"

    def get_uplaod_path(self, filename):
        file_extension = pathlib.Path(filename).suffix
        return 'uploads/profile_images/{}'.format(str(self.id)+file_extension)

    username = None
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(null=True, blank=True, default=None, max_length=255)
    last_name = models.CharField(null=True, blank=True, default=None, max_length=255)
    birthDate = models.DateField(null=False, blank=False, default=datetime.now)
    imageUrl = models.ImageField(null=True, blank=True, default=None, max_length=255, storage=OverwriteStorage(), upload_to=get_uplaod_path,
                                 validators=[FileSizeValidator(max_size=5)], help_text="* Maximum upload file size 5 MB.")
    phoneNumber = models.CharField(null=True, blank=True, default=None, max_length=255)
    city = models.CharField(null=True, blank=True, default=None, max_length=255)
    job = models.CharField(null=True, blank=True, default=None, max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, null=True, max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def getFullName(self):
        return str(self.first_name) + " " + str(self.last_name)

    def preview(self):  # new
        string = '<a href="{0}" target="_blank"><img src="{0}" width="180"/></a>'.format(self.imageUrl.url)
        return mark_safe(f'{string}')

    def __str__(self):
        return self.email


class Enrollment(models.Model):
    class Meta:
        db_table = "users_enrollments"
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        unique_together = ['user', 'course']

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(
        default=datetime.now, null=False, blank=False)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, null=False, blank=False)

    def progress(self):
        lessons = self.course.lessons().all()
        complete = self.completeLessons().all()

        try:
            return len(complete) * 100 / len(lessons)
        except:
            return 0.0

    def getAverage(self):
        complete = self.completeLessons().all()

        total = 0
        for item in complete:
            total += item.result

        return total / len(complete)

    def isComplete(self) -> bool:
        return self.progress() == 100

    def completeLessons(self):
        list = CompleteLesson.objects.filter(enrollment=self)
        return list

    @property
    def currentLesson(self):
        lessons = self.course.lessons().order_by('ordering')
        complete = list(map(lambda x: x.lesson, self.completeLessons().all()))
        for item in lessons:
            if item not in complete:
                return item

        return lessons.first()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user) + "--" + str(self.course)


class CompleteLesson(models.Model):
    class Meta:
        verbose_name = 'Complete Lesson'
        verbose_name_plural = 'Complete Lessons'
        db_table = "_enrollment_lesson_"
        unique_together = ['enrollment', 'lesson']

    enrollment = models.ForeignKey(
        Enrollment, on_delete=models.CASCADE)
    lesson = models.ForeignKey("courses.Lesson", on_delete=models.CASCADE,)
    result = models.FloatField(
        default=70.0,
        validators=[
            MinValueValidator(70),
            MaxValueValidator(100)
        ]
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # check if the course is completed
        isComplete = self.enrollment.isComplete()
        if isComplete:
            # if the course is completed create a new
            # certificate if not exists
            user = self.enrollment.user
            course = self.enrollment.course

            obj = Certificate.objects.filter(user=user, course=course).first()

            if obj is None:
                certificate = Certificate()
                certificate.user = user
                certificate.course = course
                certificate.result = self.enrollment.getAverage()
                certificate.save()

            print(self.enrollment.getAverage())

    def __str__(self):
        return str(self.lesson)


class Certificate(models.Model):
    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
        unique_together = ['user', 'course']

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(
        "courses.Course", on_delete=models.SET_NULL, null=True, blank=True)
    result = models.FloatField(
        default=70.0,
        validators=[
            MinValueValidator(70),
            MaxValueValidator(100)
        ]
    )
    date = models.DateTimeField(null=False, blank=False, auto_now=True)

    def title(self):
        return self.course.title

    def __str__(self):
        return str(self.user) + " | " + str(self.course)


class CourseBookmark(models.Model):
    class Meta:
        verbose_name = "Course Bookmark"
        verbose_name_plural = "Course Bookmarks"
        unique_together = ['user', 'course']

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(
        "courses.Course", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.course)


class DocumentBookmark(models.Model):
    class Meta:
        verbose_name = "Document Bookmark"
        verbose_name_plural = "Document Bookmarks"
        unique_together = ['user', 'document']

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.ForeignKey(
        "documents.Document", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.document)
