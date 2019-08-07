from django.db import models
import uuid
from django.utils import timezone
from offices.models import Office

# Create your models here.
class Member(models.Model):

    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" Name: {self.name} "
