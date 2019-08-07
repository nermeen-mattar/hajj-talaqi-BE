from rest_framework import serializers
from .models import Member
from rest_framework import filters

class MembersSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'
        filter_backends = [filters.SearchFilter]

        search_fields = ['=office']
        # fields = ('name', 'email', 'phone_number')