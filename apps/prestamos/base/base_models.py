from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        abstract = True
    
    def delete(self):
        self.deleted = True
        self.save()
