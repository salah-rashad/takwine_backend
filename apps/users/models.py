from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from ..courses.models import Course, Lesson, Material
from .managers import UserManager

GENDER_CHOICES = (
    ("m", "Male"),
    ("f", "Female")
)


class User(AbstractUser, PermissionsMixin):
    class Meta:
        db_table = "users"

    username = None
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    birthDate = models.DateField(null=True, blank=True, max_length=255)
    imageUrl = models.CharField(null=True, blank=True, max_length=500)
    phoneNumber = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    job = models.CharField(null=True, blank=True, max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES,
                              blank=True,
                              null=True,
                              max_length=50,
                              )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class EnrolledCourse(models.Model):
    class Meta:
        db_table = "users_enrolled_courses"
        verbose_name = 'Enrolled Course'
        verbose_name_plural = 'Enrolled Courses'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    currentLesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, null=True,)
    currentMaterial = models.ForeignKey(
        Material, on_delete=models.CASCADE, null=True,)
    progress = models.FloatField(null=False, blank=False, default=0.0)

    def __str__(self):
        return self.course.title
