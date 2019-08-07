from django.db import models
from django.utils import timezone
from reservation_scans.models import ReservationScan
from members.models import Member
import uuid
from offices.models import Office
from supervisor.models import Supervisor
# Create your models here.
class Scan(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,  editable=False)
    scanned_at = models.DateTimeField(max_length=100)
    member_id = models.ForeignKey( Member, on_delete=models.CASCADE)
    reservation_scans_id = models.ForeignKey(ReservationScan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    def __str__(self):
        return f" at: {self.scanned_at} "
