from django.db import models

from .question_choice import QuestionChoice


class Question(models.Model):
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    exam = models.ForeignKey(
        "courses.Exam", on_delete=models.CASCADE, related_name="exam_questions")

    title = models.CharField(null=False, blank=True, max_length=255)
    answer = models.ForeignKey(
        QuestionChoice,
        on_delete=models.RESTRICT,
        related_name="questions",
        null=True,
        blank=True,
    )

    def choices(self):
        list = QuestionChoice.objects.filter(
            question__id=self.id).order_by("ordering")
        return list

    def __str__(self):
        return self.title
