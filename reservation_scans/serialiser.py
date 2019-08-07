from rest_framework import serializers
from .models import ReservationScan

class ReservationScansSerialiser(serializers.ModelSerializer):



    class Meta:
        model = ReservationScan
        fields = '__all__'