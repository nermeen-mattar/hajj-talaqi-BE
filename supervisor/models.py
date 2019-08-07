from django.db import models
import uuid
from django.utils import timezone
from offices.models import Office


# Create your models here.
class Supervisor(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" Name: {self.name} "