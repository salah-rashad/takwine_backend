from django.db import models
from model_clone import CloneMixin


class QuestionChoice(CloneMixin, models.Model):
    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
        ordering = ["ordering"]
        unique_together = ["question", "name"]

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    question = models.ForeignKey("courses.Question", on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=False,
                            default=None, max_length=255)

    def __str__(self):
        return self.name
