from django.db import models





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
