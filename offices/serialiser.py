from rest_framework import serializers
from .models import Office


class OfficesSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = '__all__'
        # fields = ('name', 'email', 'phone_number')