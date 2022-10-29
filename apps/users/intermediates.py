from django.db import models


class CompleteLesson(models.Model):
    class Meta:
        verbose_name = 'Complete Lesson'
        verbose_name_plural = 'Complete Lessons'
        db_table = "_enrollment_lesson_"
        unique_together = ['enrollment', 'lesson']

    enrollment = models.ForeignKey(
        "users.Enrollment", on_delete=models.CASCADE)
    lesson = models.ForeignKey("courses.Lesson", on_delete=models.CASCADE,)
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.lesson)


# class Rel_Enrollment_Material(models.Model):
#     class Meta:
#         verbose_name = 'Complete Material'
#         verbose_name_plural = 'Complete Materials'
#         db_table = "_enrollment_material_"
#         unique_together = ['enrollment', 'material']

#     enrollment = models.ForeignKey(
#         "users.Enrollment", on_delete=models.CASCADE,)
#     material = models.ForeignKey("courses.Material", on_delete=models.CASCADE,)

#     def __str__(self):
#         return str(self.material)
