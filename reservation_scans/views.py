# -*- coding: utf-8 -*-
from rest_framework import viewsets

from django.shortcuts import render
from .models import ReservationScan

from .serialiser import ReservationScansSerialiser
# Create your views here.

class ReservationScansViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        office = self.kwargs['office_id']
        return ReservationScan.objects.filter(office = office)
    queryset = ReservationScan.objects.all()
    serializer_class = ReservationScansSerialiser