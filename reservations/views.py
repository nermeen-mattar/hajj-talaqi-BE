# -*- coding: utf-8 -*-
from rest_framework import viewsets

from django.shortcuts import render
from .models import Reservation

from .serialiser import ReservationsSerialiser
# Create your views here.

class ReservationsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        office = self.kwargs['office_id']
        return Reservation.objects.filter(office = office)
    queryset = Reservation.objects.all().order_by("created_at")
    serializer_class = ReservationsSerialiser