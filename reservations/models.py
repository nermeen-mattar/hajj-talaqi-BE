from django.db import models
from django.utils import timezone
from containers.models import Container
from offices.models import Office
import uuid
# Create your models here.
class Reservation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,  editable=False)
    name = models.CharField(max_length=100)
    container_id = models.ForeignKey(Container, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return f" Name: {self.name} "
