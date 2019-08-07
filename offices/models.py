from django.db import models
from django.utils import timezone
import uuid
# Create your models here.
class Office(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,  editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" Name: {self.name} "
