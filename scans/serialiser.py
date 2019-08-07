from rest_framework import serializers
from .models import Scan

class ScansSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Scan
        fields = '__all__'
        # fields = ('name', 'email', 'phone_number')