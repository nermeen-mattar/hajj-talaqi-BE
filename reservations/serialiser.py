from rest_framework import serializers
from .models import Reservation

class ReservationsSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'
        # fields = ('name', 'email', 'phone_number')