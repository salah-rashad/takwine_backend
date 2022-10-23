from datetime import datetime

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from apps.users.intermediates import (Rel_Enrollment_Lesson,
                                      Rel_Enrollment_Material)

from ..courses.models.material import Material
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
    first_name = models.CharField(null=False, blank=True, max_length=255)
    last_name = models.CharField(null=False, blank=True, max_length=255)
    birthDate = models.DateField(null=False, blank=False, default=datetime.now)
    imageUrl = models.CharField(null=True, blank=True, max_length=500)
    phoneNumber = models.CharField(null=False, blank=True, max_length=255)
    city = models.CharField(null=False, blank=True, max_length=255)
    job = models.CharField(null=False, blank=True, max_length=255)
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


class Enrollment(models.Model):
    class Meta:
        db_table = "users_enrollments"
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        unique_together = ('user', 'course',)

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(
        default=datetime.now, null=False, blank=False)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, null=False, blank=False)

    currentLesson = models.ForeignKey(
        "courses.Lesson", on_delete=models.SET_NULL, null=True, blank=True)
    currentMaterial = models.ForeignKey(
        Material, on_delete=models.SET_NULL, null=True, blank=True, db_column='currentMaterialId')

    completeLessons = models.ManyToManyField(
        "courses.Lesson",
        related_name="enrollments",
        blank=True,
        through=Rel_Enrollment_Lesson,
    )
    completeMaterials = models.ManyToManyField(
        Material,
        related_name="enrollments",
        blank=True,
        through=Rel_Enrollment_Material,
    )

    def progress(self):
        lessons = self.course.lessons.all()
        complete = self.completeLessons.all()
        return len(complete) * 100 / len(lessons)

    def isComplete(self) -> bool:
        return self.progress() == 100

    def __str__(self):
        return str(self.user) + "--" + str(self.course)
