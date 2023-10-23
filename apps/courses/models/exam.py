from django.db import models
from model_clone import CloneMixin

from apps.courses.models.question import Question


class Exam(CloneMixin, models.Model):
    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'
        ordering = ['ordering', ]

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    lesson = models.ForeignKey("courses.Lesson", on_delete=models.CASCADE, related_name="exams")

    def questions(self):
        list = Question.objects.filter(lesson=self.lesson).order_by("ordering")
        return list

    def course(self):
        return self.lesson.course

    def __str__(self):
        return str(self.lesson.title)
