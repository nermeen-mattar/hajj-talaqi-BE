# -*- coding: utf-8 -*-
from rest_framework import viewsets

from django.shortcuts import render
from .models import Supervisor

from .serialiser import SupervisorsSerialiser
# Create your views here.

class SupervisorsViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        office = self.kwargs['office_id']
        return Supervisor.objects.filter(office = office)

    queryset = Supervisor.objects.all().order_by("created_at")
    serializer_class = SupervisorsSerialiser