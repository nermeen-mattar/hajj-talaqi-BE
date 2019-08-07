from rest_framework import serializers
from .models import Container

class ContainersSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Container
        fields = '__all__'
        # fields = ('name',)