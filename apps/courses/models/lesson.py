from django.db import models
from model_clone import CloneMixin

from .exam import Exam
from .material import Material


class Lesson(CloneMixin, models.Model):
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['ordering', ]

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=False,
                             default=None, max_length=255)
    description = models.CharField(
        null=True, blank=True, default=None, max_length=255)
    days = models.PositiveIntegerField(null=False, blank=False, default=1)
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name="lessons", null=True)

    def totalMaterialsCount(self):
        return len(self.materials().all())

    # def related_courses(self):
    #     courses = Course.objects.filter(
    #         lessons__id=self.id)
    #     return list(map(lambda x: x.title, courses))

    def materials(self):
        list = Material.objects.filter(lesson=self).order_by('ordering')
        return list

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if self.pk:
            super(Lesson, self).save(*args, **kwargs)
        else:
            super(Lesson, self).save(*args, **kwargs)
            exam = Exam(lesson=self)
            exam.save()
            self.exam = exam
            return super().save(*args, **kwargs)
