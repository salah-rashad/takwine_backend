# from django.db import models

# class SoftDeleteManager(models.Manager):
#   def __init__(self, *args, **kwargs):
#     self.with_deleted = kwargs.pop('deleted', False)
#     super(SoftDeleteManager, self).__init__(*args, **kwargs)

#   def _base_queryset(self):
#     return super().get_queryset().filter(deleted_at=None)

#   def get_queryset(self):
#     qs = self._base_queryset()
#     if self.with_deleted:
#       return qs
#     return qs.filter(is_deleted=False)


# class SoftDeleteModel(BaseModel):
#   class meta:
#       abstract = True
  
#   objects = SoftDeleteManager()
#   objects_with_deleted = SoftDeleteManager(deleted=True)
        
#   is_deleted = models.BooleanField(null=False, default=False)

#   def delete(self):
#     self.is_deleted = True
#     self.save()

#   def restore(self):
#     self.is_deleted = False
#     self.save()