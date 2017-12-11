import uuid
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class DefaultBaseModel(TimestampedModel):
    slug = models.SlugField(max_length=36, unique=True, default=uuid.uuid4())
    description = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        abstract = True
        ordering = ['slug', 'name']

