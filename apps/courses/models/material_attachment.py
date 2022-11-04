# from django.db import models


# class MaterialAttachment(models.Model):
#     class Meta:
#         verbose_name = 'Attachment'
#         verbose_name_plural = 'Material Attachments'
#         db_table = "courses_material_attachment"
#         ordering = ['ordering']

#     ordering = models.PositiveIntegerField(
#         default=0,
#         blank=False,
#         null=False,
#         db_index=True,
#     )

#     material = models.ForeignKey("courses.Material", on_delete=models.CASCADE)

#     name = models.CharField(null=True, blank=True, default=None, max_length=255)
#     url = models.CharField(null=True, blank=True, default=None, max_length=255)
#     date = models.DateTimeField(null=False, blank=False, auto_now_add=True)

#     def __str__(self):
#         return str(self.name)
