from django.db import models
import uuid
from django.utils import timezone


# Create your models here.
class Container(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    default = models.BooleanField()
    icon = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" Name: {self.name} "
