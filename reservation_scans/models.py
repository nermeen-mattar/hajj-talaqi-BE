from django.db import models
from django.utils import timezone
from reservations.models import Reservation
import uuid
from offices.models import Office
# Create your models here.
class ReservationScan(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,  editable=False)
    name = models.CharField(max_length=100)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return f" Name: {self.name}, office: {self.office.name}, reservation:  {self.reservation.name}" 
