from rest_framework import serializers
from .models import ReservationScan

class ReservationScansSerialiser(serializers.Serializer):



    class Meta:
        model = ReservationScan
        fields = '__all__'
        # fields = ('name', 'email', 'phone_number')