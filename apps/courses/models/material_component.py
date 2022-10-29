# from django.db import models

# COMPONENT_TYPE_CHOICES = (
#     ("text", "Text"),
#     ("image", "Image"),
#     ("video", "Video"),
# )


# class MaterialComponent(models.Model):
#     class Meta:
#         verbose_name = 'Component'
#         verbose_name_plural = 'Material Components'
#         db_table = "courses_material_component"
#         ordering = ['ordering']

#     ordering = models.PositiveIntegerField(
#         default=0,
#         blank=False,
#         null=False,
#         db_index=True,
#     )
    
#     material = models.ForeignKey("courses.Material", on_delete=models.CASCADE)

#     type = models.CharField(
#         choices=COMPONENT_TYPE_CHOICES,
#         blank=False,
#         null=False,
#         default=COMPONENT_TYPE_CHOICES[0][0],
#         max_length=50,
#     )
#     data = models.TextField(null=False, blank=True, max_length=550)

#     def __str__(self):
#         return "{}: {}".format(self.type, self.data[0:30])
