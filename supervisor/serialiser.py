from rest_framework import serializers
from .models import Supervisor

class SupervisorsSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Supervisor
        fields = '__all__'
        # fields = ('name',)