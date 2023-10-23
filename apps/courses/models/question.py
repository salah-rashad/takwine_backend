from django.db import models
from model_clone import CloneMixin

from .question_choice import QuestionChoice


class Question(CloneMixin, models.Model):
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Exam Questions"
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    lesson = models.ForeignKey(
        "courses.Lesson", on_delete=models.CASCADE, related_name="exam_questions",)

    title = models.CharField(null=True, blank=False,
                             default=None, max_length=255)
    answer = models.ForeignKey(
        QuestionChoice,
        on_delete=models.RESTRICT,
        related_name="questions",
        null=True,
        blank=True,
    )

    def choices(self):
        list = QuestionChoice.objects.filter(
            question=self).order_by("ordering")
        return list

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        answer = self.answer
        choices = self.choices()

        if choices:
            if answer is None:
                self.answer = choices.first()
        else:
            defaultChoice = QuestionChoice(name="choice 1", question=self)
            defaultChoice.save()
            self.answer = defaultChoice
        super().save(*args, **kwargs)

    def __str__(self):
        try:
            if self.answer:
                return self.title
            else:
                return str("🛑 ") + str(self.title)
        except:
            return self.title
